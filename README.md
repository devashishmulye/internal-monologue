# internal-monologue
All developers work on difficult projects that need focus.
All developers get numerous random thoughts in the middle of it.
All developers always have their terminal open.

Internal Monologue is a single-command cli tool that enables developers to swiftly log their random unrelated thoughts via their terminal with minimum cognitive diversion. They can then later check these thoughts in a Trello Board when they have the time.



## How to set up internal monologue
You can use internal monologue by 3 easy steps.

(You have to be logged into your trello account to see below linked accounts)
1. Generate your [Trello API Key](https://trello.com/app-key) and [Trello Temporary Token](https://trello.com/1/authorize?expiration=never&scope=read,write,account&response_type=token&name=Server%20Token&key=efbd634e254c0250a96e4ac948616f12).

*You can use the temporary trello token since this app works completely on your local and its only for your own personal use. There is no server. The source code is also available in the repo if you would like to check how it works under the hood*

2. export your credentials in your bash_profile in the following way

		export TRELLO_API_KEY="<YOUR_TRELLO_API_KEY_HERE>"

		export TEMPORARY_TRELLO_TOKEN="<YOU_TEMPORARY_TRELLO_TOKEN>"


3. Install the pip package for internalmonologue

		pip3 install internalmonologue

## How to use

Simply go to your terminal window and type 

		logue reminder to pay electricity bill

and "reminder to pay electricity bill" will appear in a trello board called `Internal Monologue`

## ROADMAP

- [ ] Adding labels to your logues so they are automatically sorted when you open your trello board at the end of the day
- [ ] Creating a similar tool which uses google docs instead of trello.


*Inspired by an idea by Srihari Radhakrishna(n?)*


