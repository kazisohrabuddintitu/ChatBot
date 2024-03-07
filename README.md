# ChatBot

## Overview

The PDF Chatbot Project is a Django-based web application that integrates a chatbot to answer user queries based on uploaded PDF documents. It provides a RESTful API for communication and includes a Streamlit-based frontend for a user-friendly interface.

## Table of Contents

- [Approach](#approach)
- [Architecture Diagram](#architecture-diagram)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Future Scope](#future-scope)

## Approach

The project follows a client-server architecture, where the Django backend serves as the API provider, handling both existing sessions and new chat logs. The Streamlit frontend interacts with the API to display old and new chats. Used `Hugging Face Pipeline` for question answering.

### Key Components

- **Django Backend:**
  - Manages sessions and chat logs in the database.
  - Provides RESTful API endpoints for existing sessions and new chat logs.

- **Streamlit Frontend:**
  - Allows users to input session ID, upload PDFs, and ask questions.
  - Displays old and new chats retrieved from the Django backend.

- **Chatbot Utility:**
  - Processes user questions based on session ID and PDF content.

## Architecture Diagram

![Project Architecture Diagram](Phots/chatbot.jpg)

## Screenshots

![Front page](Phots/1st.png)
![New pdf and session id](Phots/new.png)
![Already existed pdf](Phots/existing.png)


## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kazisohrabuddintitu/ChatBot.git

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install backend dependencies:**
    ```bash
    pip install -r requirements.txt   

4. **Direct to project folder**
    ```bash
    cd chatbot_project

5. **Apply Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate

6. **Create a Superuser (Optional):**
    ```bash
    python manage.py createsuperuser

7. **Run the Django development server:**
    ```bash
    python manage.py runserver
    The API will be accessible at http://localhost:8000/api/.

8. **Open another terminal for streamlit_app**
    ```bash
    streamlit run streamlit_app.py
    The UI will be accessible at Local URL: http://localhost:8501
    Network URL: http://192.168.0.102:8501


## Future Scope
### User Authentication:
    - Implement user authentication for secure access and personalized chat history.
### PDF Parsing Enhancements:
    - Improve PDF parsing capabilities for more accurate responses.
### Natural Language Processing (NLP):
    - Integrate NLP techniques for better understanding and context-aware responses.
### Deployment:
    - Deploy the application to production servers for public access.
