import chainlit as cl
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain.schema import StrOutputParser

# local
from prompt import prompt
from schema import Invoice


@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content="Hello, I'm your virtual assistant Lara and I do the bookkeeping for you. Should I write an invoice or post an incoming or outgoing invoice?"
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    model = ChatOpenAI(streaming=True)
    parser = JsonOutputParser(pydantic_model=Invoice)
    chain = prompt | model | StrOutputParser()
    result = chain.invoke(
        {
            "question": message.content,
            "format_instructions": parser.get_format_instructions(),
        }
    )
    await cl.Message(content=result).send()
