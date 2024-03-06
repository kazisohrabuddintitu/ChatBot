from django.conf import settings
import os
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
import pdfplumber

BASE_DIR = settings.BASE_DIR

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def process_question(session_id, pdf_text, query_question):
    # Explicitly specify the model name and revision
    model_name = "distilbert-base-cased-distilled-squad"
    revision = "626af31"

    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name, revision=revision)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name, revision=revision)

    # Create the question-answering pipeline
    qa_model = pipeline("question-answering", model=model, tokenizer=tokenizer)
    
    # Processing the question using the question-answering pipeline
    response = qa_model(question=query_question, context=pdf_text)
    response_text = response['answer']

    return response_text
