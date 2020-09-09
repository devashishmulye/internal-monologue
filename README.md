# internal-monologue
Internal Monologue is a tool for developers to quickly log what may randomly appear in their mind while they are in the middle of an otherwise important task. You can log your thoughts via the terminal and finally see them all in Trello at the end of the day.


## How to set up internal monologue
You can use internal monologue by 3 easy steps.

1. Generate your [Trello API Key](https://trello.com/app-key) and [Trello Temporary Token](https://trello.com/1/authorize?expiration=never&scope=read,write,account&response_type=token&name=Server%20Token&key=efbd634e254c0250a96e4ac948616f12).

*You can use the temporary trello token since this app works completely on your local and its only for your own personal use. There is no server. The source code is also available in the repo if you would like to check how it works under the hood*

2. export your credentials in your bash_profile in the following way

		export TRELLO_API_KEY="<YOUR_TRELLO_API_KEY_HERE>"

		export TEMPORARY_TRELLO_TOKEN="<YOU_TEMPORARY_TRELLO_TOKEN>"


3. Copy the executable file to your bin

		cp dist/logue ~/bin/logue

## How to use

Simply go to your terminal window and type 

		logue reminder to pay electricity bill

and it will appear in a trello board called `Internal Monologue`

## ROADMAP

1. Adding labels to your logues so they are automatically sorted when you open your trello board at the end of the day
2. Creating a similar tool which uses google docs instead of trello.



