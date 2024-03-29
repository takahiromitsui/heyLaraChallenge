
# HeyLara Coding Challenge
I created a chatbot that fills a JSON-structure based on a conversation with a user.

- Total time: 4 hours (excluding time for documents).
![time](https://github.com/takahiromitsui/heyLaraChallenge/assets/78789212/af19bd3f-c1d0-4120-aea1-f4520e54f5aa)




## Environment Variables

To run this project, you must add the following environment variables to your .env file (see .env.example).

Chainlit automatically loads env variables. Therefore, I did not have to add `python-dotenv` (see src/main.py).

`OPENAI_API_KEY`


## Run Locally
This application uses [poetry](https://python-poetry.org/docs/#installation) for dependency management and packaging in Python.

- Python 3.11≤
- poetry

Clone the project

```bash
  git clone https://github.com/takahiromitsui/heyLaraChallenge.git
```

Once you have installed the prerequisites:

```bash
  # Create a virtual environment
  $ poetry shell
  # Install all packages
  $ poetry install
  # Run application
  $ poetry run chainlit run src/app.py -w
```


## Folder Structure

    ├── src                     
        ├── app.py.   # I created life cycles for Chainlit. Also, I added logic to connect GPT3 and to process data.              
        ├── schema.py # I defined pydantic schemas for JSON.
    └── pyproject.toml # All dependecies




## Limitation

### 1. AI agent always returns JSON format.
For example, users will get an empty JSON when they ask random questions.

I defined `parser` with JsonOutputParser(`line 44 on app.py`), and the chatbot will format the answer to JSON.

Therefore, I need to change the flexible parser depending on user input on production.

e.g.,

![1](https://github.com/takahiromitsui/heyLaraChallenge/assets/78789212/9cb65e28-ec96-4370-aa62-70d827d87b76)

### 2. PDF export.
I have yet to finish implementing the PDF export in 4 hours.

So, I added a logic to detect "pdf" in user questions and returned the sentence "Sorry, this feature is not implemented yet.".

In future production, I'll add a PDF export function in this section or will check if the JSON is filled and ask users if they want to export PDF.
![2](https://github.com/takahiromitsui/heyLaraChallenge/assets/78789212/e3183e79-0f95-402b-882f-e983b1ecaede)

## Production idea
### 1. Add custom UIs
I utilised Chainlit default UIs to build up the chatbot. However, we must use the original design for branding.

Chainlit allows to customise UI with React ([link](https://docs.chainlit.io/customisation/react-frontend)). Therefore, I'll tweak the front end using React.
 
### 2. Memory management
I used session functionality to store output JSON (see `line 52 on app.py`) so that I could update JSON by conversation.

However, we could take advantage of previous conversations instead.

For instance, we can trace previous conversation summaries using [ConversationSummaryBufferMemory](https://python.langchain.com/docs/modules/memory/types/summary_buffer) from langchain.

### 3. Speed?
Speed is crucial for LLM applications, and ChatGPT operates on GPUs. 

However, [Groq](https://wow.groq.com/why-groq/) offers LPU, a processor designed for LLMs, which delivers exceptional speed. 

Connecting to Groq's API could enhance speed further.



