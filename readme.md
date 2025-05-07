# ShopBot – Dialogflow + Django Chatbot for Product Pricing

ShopBot is an intelligent chatbot that helps users get real-time product prices by integrating Dialogflow with a Django backend. It reads product information from a live database and replies instantly via webhooks.

---

## Features

- Ask natural questions like: "What is the price of a shirt?"
- Real-time price lookup from Django database
- Dialogflow integration via webhooks
- Automatically reflects price changes in database
- Simple, customizable Django backend

---

## Tech Stack

- Python 3.12
- Django
- Dialogflow (CX or ES)
- SQLite (default, can use PostgreSQL/MySQL)
- Ngrok (for local webhook testing)

---

## Getting Started

### 1. Clone the repository

```bash
git repo -> https://github.com/manas9568/chatbot.git
cd shopbot
```

## Set up virtual environment

```bash
python -m venv env
source env/bin/activate  # or env\\Scripts\\activate on Windows
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run Migrations

```bash

python manage.py makemigrations
python manage.py migrate
```

## Start Django server

```bash
python manage.py runserver
```

## Dialogflow Setup

```bash
1-> Create a agent is Dialogflow.
2-> Enable webhook fulfillment and point it to your Django endpoint (e.g., via ngrok):

ngrok http 8000

3-> In your intent (e.g., Price), enable webhook call and set up a parameter like product.

```
