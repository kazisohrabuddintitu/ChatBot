import streamlit as st
import requests
import os

st.title("PDF Chatbot")

session_id = st.text_input("Enter Session ID:")
pdf_file = st.file_uploader("Upload PDF", type=["pdf"])
question = st.text_input("Enter Your Question:")

if st.button("Get Response"):
    if session_id or question or pdf_file:

        # Determining whether to use the existing PDF or the uploaded PDF
        if pdf_file:
            # Save the uploaded PDF to the Django MEDIA_ROOT directory
            pdf_path = os.path.abspath(os.path.join("..", "chatbot_project", "uploads", pdf_file.name))
            with open(pdf_path, "wb") as pdf_writer:
                pdf_writer.write(pdf_file.read())

            # If PDF is provided, call the new chat log creation API
            new_chat_url = f"http://127.0.0.1:8000/api/new_chatlog/{session_id}/{pdf_file.name}/{question}/"
            data = {"session_id": session_id, "pdf_name": pdf_file.name, "query_question": question}
            response = requests.post(new_chat_url, json=data).json()
            
        else:
            # Making API call to the FastAPI endpoint hosted by Django
            api_url = f"http://127.0.0.1:8000/api/chatlog/{session_id}/{question}/"
            
            # If PDF is not provided, call the existing session ID API
            data = {"session": {"session_id": session_id}, "query_question": question}
            response = requests.post(api_url, json=data).json()

        # Display old and new chats
        st.text("Old Chats:")
        for chat in response.get("old_chats", []):
            st.text(chat)

        st.text("New Chat:")
        st.text(response.get("response_text", ""))
