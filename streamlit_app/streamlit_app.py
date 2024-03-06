import streamlit as st
import requests
import os

st.title("PDF Chatbot")

session_id = st.text_input("Enter Session ID:")
pdf_file = st.file_uploader("Upload PDF", type=["pdf"])
question = st.text_input("Enter Your Question:")

if st.button("Get Response"):
    if session_id and question:
        # Check if session exists
        session_check_url = f"http://127.0.0.1:8000/api/check_session_exists/{session_id}/"
        session_response = requests.get(session_check_url).json()

        if session_response.get("session_exists", False):
            # If session exists, use the old PDF
            pdf_file = None

        # Making API call to the FastAPI endpoint hosted by Django
        api_url = f"http://127.0.0.1:8000/api/chatlog/{session_id}/"

        # Send data in the request body
        data = {"session_id": session_id, "pdf_name": pdf_file.name if pdf_file else None, "query_question": question}
        response = requests.post(api_url, json=data).json()

        # Display old and new chats
        st.text("Old Chats:")
        for chat in response.get("old_chats", []):
            st.text(chat)

        st.text("New Chat:")
        st.text(response.get("new_chat", ""))
