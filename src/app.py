import chainlit as cl
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain.schema import StrOutputParser
from langchain.prompts import PromptTemplate

# local
# from prompt import prompt
from schema import Invoice


@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content="Hello, I'm your virtual assistant Lara and I do the bookkeeping for you. Should I write an invoice or post an incoming or outgoing invoice?"
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    model = ChatOpenAI(streaming=True, temperature=0)
    parser = JsonOutputParser(pydantic_model=Invoice)
    prompt = PromptTemplate(
        template="Answer the user query.\n{format_instructions}\n{query}\n",
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    chain = prompt | model | parser
    result = chain.invoke(
        {
            "query": message.content,
        }
    )
    await cl.Message(content=result).send()
