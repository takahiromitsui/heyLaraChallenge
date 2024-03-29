import chainlit as cl
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate

# local
# from prompt import prompt
from schema import Invoice


@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("invoice", Invoice())
    await cl.Message(
        content="Hello, I'm your virtual assistant Lara and I do the bookkeeping for you. Should I write an invoice or post an incoming or outgoing invoice?"
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    model = ChatOpenAI(streaming=True, temperature=0)
    # parser = JsonOutputParser(pydantic_model=Invoice)
    pydantic_parser = PydanticOutputParser(pydantic_object=Invoice)
    format_instructions = pydantic_parser.get_format_instructions()
    previous_invoice = cl.user_session.get("invoice")

    template_string = """
    You are creating an invoice. 
    Please fill in the following fields based on user query and the format instructions below.
    {format_instructions}
    {query}
    But, do not make up any information. If you don't know the answer, just fill null.
    But if there is a previous invoice in the session, update the fields with the new information.
    {previous_invoice}
    Return the invoice as a JSON object.
    """
    prompt = ChatPromptTemplate.from_template(template=template_string)
    chain = prompt | model | JsonOutputParser(pydantic_model=Invoice)
    result = chain.invoke(
        {
            "query": message.content,
            "format_instructions": format_instructions,
            "previous_invoice": previous_invoice,
        }
    )
    cl.user_session.set("invoice", result)
    # print(result)
    await cl.Message(content=result).send()
