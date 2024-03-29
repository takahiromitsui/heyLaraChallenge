import chainlit as cl
from langchain_openai import ChatOpenAI

# local
from prompt import prompt


@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content="Hello, I'm your virtual assistant Lara and I do the bookkeeping for you. Should I write an invoice or post an incoming or outgoing invoice?"
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    model = ChatOpenAI(streaming=True)
    chain = prompt | model
    result = chain.invoke({"question": message.content})
    await cl.Message(content=result).send()
