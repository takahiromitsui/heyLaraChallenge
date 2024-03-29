
# HeyLara Coding Challenge
I create a chatbot that fills a json-structure, based on a conversation with a user.

- Total amount of time: 4h (excluding time for documents)



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file (see .env.example).

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
  # poetry run chainlit run src/app.py -w
```


## Folder Structure

    ├── src                     
        ├── app.py.   # I created life cycles for chainlit. Also, added logic for user input to GPT-3 and output processing.GPT3.                
        ├── schema.py # I defined pydantic schemas for JSON.
    └── pyproject.toml # All dependecies






## Limitation
