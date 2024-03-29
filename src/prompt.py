from langchain.prompts.chat import ChatPromptTemplate

human_template = """
  {question}
"""

prompt = ChatPromptTemplate.from_messages([("human", human_template)])
