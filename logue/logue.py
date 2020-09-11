
from datetime import datetime
import requests
import sys
import os
import json




BOARD_ID_JSON = "board_id.json"
BOARD_NAME = "Internal Monologue"



API_KEY = os.environ.get('TRELLO_API_KEY')
TEMPORARY_TOKEN = os.environ.get("TEMPORARY_TRELLO_TOKEN")

if API_KEY is None or TEMPORARY_TOKEN is None:
    print ("Please export TRELLO_API_KEY and TEMPORARY_TRELLO_TOKEN in your environment variables")
    print ("Refer to README for the 2 easy steps")

def save_board_id_in_local(board_id,url):
    with open(BOARD_ID_JSON, "w") as board_id_dict:
        json.dump({"board_id": board_id,"url":url}, board_id_dict)



def get_board_id_from_json():
    files = os.listdir(os.getcwd())
    for item in files:
        if item == BOARD_ID_JSON:
            with open(BOARD_ID_JSON, "r") as board_id_dict:
                board_id_dict = json.load(board_id_dict)
            return board_id_dict["board_id"], board_id_dict["url"]
    else:
        return None, None

def list_board_ids():
    url = "https://api.trello.com/1/members/me/boards"
    querystring = {"key": API_KEY,
                   "token": TEMPORARY_TOKEN}
    response = requests.request("GET", url, params=querystring)
    # print response.text
    boards = response.json()
    return boards


def get_internal_monologue_board():
    board_list_response = list_board_ids()
    for board in board_list_response:
        if board['name'] == BOARD_NAME:
            board_id = board["id"]
            url = board['shortUrl']
            save_board_id_in_local(board_id,url)
            print ("This logue is taking longer, since it is also getting info on the resources required.")
            return board_id, url
    return None, None




def create_board():
    url = "https://api.trello.com/1/boards"
    board_name = BOARD_NAME
    querystring = {"name": board_name, "key": API_KEY, "token": TEMPORARY_TOKEN}
    response = requests.request("POST", url, params=querystring)
    board_id = response.json()["id"]
    url = response.json()["shortUrl"]
    print ("Creating a Board for you by the name {}. This is a one-time thing.".format(BOARD_NAME))
    print ("You can view the board here {}".format(url))
    print ("The first logue takes longer, since it is also creating the resources required")
    save_board_id_in_local(board_id,url)
    return board_id, url

def get_board_id():
    board_id, url = get_board_id_from_json()
    if board_id is not None:
        return board_id, url

    board_id, url = get_internal_monologue_board()
    if board_id is not None:
        return board_id, url

    board_id, url =  create_board()
    return board_id, url



BOARD_ID, URL = get_board_id()




def create_todays_list():
    list_name = get_list_name()
    url = "https://api.trello.com/1/lists"
    querystring = {"name":list_name,"idBoard":BOARD_ID,"key":API_KEY,"token":TEMPORARY_TOKEN}
    response = requests.request("POST", url, params=querystring)
    list_id = response.json()["id"]
    return list_id


def create_card(list_id, input_string):
    url = "https://api.trello.com/1/cards"
    querystring = {"idList": list_id, "key": API_KEY, "token": TEMPORARY_TOKEN, "name": input_string}
    response = requests.request("POST", url, params=querystring)
    return True

def get_list_name():
    today_date = datetime.now()
    return  today_date.strftime("%d %B %Y")


def check_if_list_exists():
    card_name = get_list_name()
    # print "Card Name"
    all_trello_lists = get_all_trello_lists()
    for trello_list in all_trello_lists:
        list_name = trello_list["name"]
        list_id = trello_list["id"]
        if list_name == card_name:
            return True, list_id
    return False, None




def get_all_trello_lists():
    url = "https://api.trello.com/1/boards/{}/lists".format(BOARD_ID)
    querystring = {"cards": "none", "key": API_KEY,
                   "token": TEMPORARY_TOKEN}
    response = requests.request("GET", url, params=querystring)

    # print response.text

    response_json = response.json()
    return response_json




def process_input(input_string):
    is_list_exist, list_id = check_if_list_exists()
    if is_list_exist is False:
        list_id = create_todays_list()

    create_card(list_id,input_string)
    return True


def main():
    input_string = ''
    for ind, arg in enumerate(sys.argv):
        if ind == 0:
            continue
        if ind == 1:
            input_string += str(arg)
        else:
            input_string += ' ' + str(arg)

    if input_string == 'dashboard':
        print ("You trello board name is {}.".format(BOARD_NAME))
        print ("You can view the board here {}".format(URL))
    else:
        process_input(input_string)


if __name__ == '__main__':
    main()









