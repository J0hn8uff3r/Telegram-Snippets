'''
This snippet reply to specific user ids, with a custom message every time someone from the user list sends you something.
'''
from pyrogram import Client, filters

app = Client("client")


USER_LIST_IDS = []

CUSTOM_MESSAGE = "<b>Automated message:</b> I'm not available by the moment, leave your message and I will answer you asap."


@app.on_message(filters.private & filters.user(USER_LIST_IDS))
def echo(client, message):
    message.reply(CUSTOM_MESSAGE)


app.run()
