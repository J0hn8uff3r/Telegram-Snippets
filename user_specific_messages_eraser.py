'''
This snippet deletes incoming text messages (for both sides) from specific user ids, using filters to delete just text messages contained in a forbidden words list
'''
from pyrogram import Client, filters

USER_LIST_IDS = []

FORBIDDEN_WORDS = ["hola", "xd"]

app = Client("client")


@app.on_message(filters.text & filters.chat(USER_LIST_IDS) & ~filters.user("me"))
def delete_message(client, message):
    if any(
            map(message.text.lower().__contains__, FORBIDDEN_WORDS)):
        try:
            app.delete_messages(
                chat_id=message.from_user.id,
                message_ids=message.message_id,
                revoke=True
            )
        except Exception as e:
            print(e)
            pass


app.run()
