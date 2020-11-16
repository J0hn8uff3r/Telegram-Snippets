'''
This snippet moves (editing) an outgoing text message sent after /m command to simulate a text movement.
'''
from pyrogram import Client, filters
from time import sleep

app = Client("client")


@app.on_message(filters.outgoing & filters.command('m'))
def mover(client, message):
    text = message.text
    text = text.replace("/m", "")
    text = text.replace(" ", "_")
    client.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text=text
    )
    for i in range(len(text) * 10):
        f = text[0]
        text = text[1:]
        text += f
        client.edit_message_text(
            chat_id=message.chat.id,
            message_id=message.message_id,
            text=text
        )
        sleep(0.4)


app.run()
