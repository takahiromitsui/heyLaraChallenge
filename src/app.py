import chainlit as cl

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content="Hello, I'm your virtual assistant Lara and I do the bookkeeping for you. Should I write an invoice or post an incoming or outgoing invoice?"
    ).send()