from langchain.prompts.chat import ChatPromptTemplate

system_template = """
  Hello,
  I'm your virtual assistant Lara and I do the bookkeeping for you.
  Should I write an invoice or post an incoming or outgoing invoice?
"""

human_template = """
  Fill in None if you don't know the answer.
  {question}
  {format_instructions}
"""

prompt = ChatPromptTemplate.from_messages(
    [("system", system_template), ("human", human_template)]
)
