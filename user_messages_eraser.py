'''
This snippet deletes incoming text messages using filters to delete just text messages from specific groups and user ids
'''
from pyrogram import Client, filters

USER_LIST_IDS = []

GROUP_IDS = []

app = Client("client")


@app.on_message(filters.text & filters.chat(GROUP_IDS) & filters.user(USER_LIST_IDS))
def delete_message(client, message):
    try:
        app.delete_messages(
            chat_id=message.chat.id,
            message_ids=message.message_id
        )
    except Exception as e:
        print(e)
        pass


app.run()
