# ImageBot

ImageBot creates images

# Getting Started

To get started with this project, you'll need to clone the repository and set up a virtual environment. This will allow you to install the required dependencies without affecting your system-wide Python installation.

### Cloning the Repository

    git clone https://github.com/jkmathilda/ImageBot.git

### Setting up a Virtual Environment

    cd ./ChatGPT-Chatbot

    pyenv versions

    pyenv local 3.11.6

    echo '.env'  >> .gitignore
    echo '.venv' >> .gitignore

    ls -la

    python -m venv .venv        # create a new virtual environment

    source .venv/bin/activate   # Activate the virtual environment

    python -V                   # Check a python version

### Install the required dependencies

    pip install -r requirements.txt

### Configure the Application

To configure the application, there are a few properties that can be set the environment

    echo 'OPENAI_API_KEY="sk-...."' >> .env

### Running the Application

    python -m streamlit run main.py

### Deactivate the virtual environment

    deactivate

# Example

![Image 2023-12-26 at 1 08 PM](https://github.com/jkmathilda/ImageBot/assets/142202145/6bdb0578-2af3-4b41-9827-dc537a2a3fa9)

# Reference

OpenAI Soure
https://platform.openai.com/docs/guides/images/usage
