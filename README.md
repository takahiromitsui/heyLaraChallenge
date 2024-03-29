
# HeyLara Coding Challenge
I created a chatbot that fills a JSON-structure based on a conversation with a user.

- Total time: 4 hours (excluding time for documents).
![time](https://github.com/takahiromitsui/heyLaraChallenge/assets/78789212/af19bd3f-c1d0-4120-aea1-f4520e54f5aa)




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

### 1.AI agent always returns JSON format.
For example, users will get an empty JSON when they ask random questions.

I defined `parser` with JsonOutputParser(`line 44 on app.py`), and the chatbot will format the answer to JSON.

Therefore, I need to change the flexible parser depending on user input on production.

e.g.,

![1](https://github.com/takahiromitsui/heyLaraChallenge/assets/78789212/9cb65e28-ec96-4370-aa62-70d827d87b76)

### 2.PDF export.
I have yet to finish implementing the PDF export in 4 hours.

So, I added a logic to detect "pdf" in user questions and returned the sentence "Sorry, this feature is not implemented yet.".

In future production, I'll add a PDF export function in this section or will check if the JSON is filled and ask users if they want to export PDF.
![2](https://github.com/takahiromitsui/heyLaraChallenge/assets/78789212/e3183e79-0f95-402b-882f-e983b1ecaede)



