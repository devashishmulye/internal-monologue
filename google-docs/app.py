from __future__ import print_function

import os
from calendar import day_name, month_abbr
from datetime import datetime

from dotenv import load_dotenv, set_key
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/documents"]

load_dotenv()


def auth():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def main():
    """Shows basic usage of the Docs API.
    Prints the title of a sample document.
    """
    creds = auth()
    service = build("docs", "v1", credentials=creds)

    # The ID of a sample document.
    DOCUMENT_ID = os.getenv("DOCUMENT_ID")

    # Retrieve the documents contents from the Docs service.
    if not DOCUMENT_ID:
        title = "Internal Monologue"
        body = {"title": title}
        doc = service.documents().create(body=body).execute()
        print("Created document with title: {0}".format(doc.get("title")))

        if not os.path.exists(".env"):
            os.write(".env")

        DOCUMENT_ID = doc.get("documentId")
        set_key(".env", "DOCUMENT_ID", DOCUMENT_ID)

    document = service.documents().get(documentId=DOCUMENT_ID).execute()

    print("The title of the document is: {}".format(document.get("title")))

    service.documents().get(documentId=DOCUMENT_ID).execute()
    today = datetime.today()
    service.documents().batchUpdate(
        documentId=DOCUMENT_ID,
        body={
            "requests": [
                {
                    "insertPageBreak": {
                        "location": {"index": 1},
                    },
                },
                {
                    "insertText": {
                        "text": f"{day_name[today.weekday()]}, {today.day} {month_abbr[today.month]} '{today.year%100}\n",
                        "location": {"index": 1},
                    },
                },
                {
                    "updateParagraphStyle": {
                        "fields": "namedStyleType",
                        "paragraphStyle": {"namedStyleType": "HEADING_1"},
                        "range": {
                            "startIndex": 1,
                            "endIndex": 2,
                        },
                    }
                },
            ]
        },
    ).execute()

    document = service.documents().get(documentId=DOCUMENT_ID).execute()
    para_index = document.get("body", {}).get("content", {})[1]["endIndex"]
    service.documents().batchUpdate(
        documentId=DOCUMENT_ID,
        body={
            "requests": [
                {
                    "insertText": {
                        "location": {"index": para_index},
                        "text": f"{datetime.now().strftime('%H:%M.%S')}",
                    }
                },
                {
                    "updateParagraphStyle": {
                        "fields": "namedStyleType",
                        "paragraphStyle": {"namedStyleType": "NORMAL_TEXT"},
                        "range": {
                            "startIndex": para_index,
                            "endIndex": para_index,
                        },
                    }
                },
            ]
        },
    ).execute()


if __name__ == "__main__":
    main()
