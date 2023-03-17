# FastAPI_Crypto_Bot

This telegram bot was designed to practice using FastAPI, integrating CRUD with databases, and learning PonyORM

**At the moment, the bot is under development**

The bot implements:
- CRUD operations over test/real btc wallets;
- Sending btc between wallets;
- Saving the history of transactions between wallets;
- Administration of users' wallets.

#

### :computer: Technologies:
- FastAPI (CRUD, Pydantic, requests);
- DataBases (SQLite, PonyORM);
- Telebot;
- Bit;
---





### :hammer_and_wrench: Installation:
1. $ pip install -r requirements.txt
2. Add the following variables to the **.env** environment, to work with the python_dotenv library:
  
       - BOT_TOKEN = <API key from Telegram bot>
       - API_URL = <URL of the FastAPI-server>
       - TG_ADMIN_ID = <Bot administrator's id>       
       
3. run app.py and tg_bot.py
