from django.conf import settings
import os
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
import pdfplumber

BASE_DIR = settings.BASE_DIR

# Function to extract text from pdf
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text


# Function to get the answer of the query question
def process_question(session_id, pdf_name, query_question):
    # specify the model name and revision
    model_name = "distilbert-base-cased-distilled-squad"
    revision = "626af31"

    # tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name, revision=revision)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name, revision=revision)

    pdf_path = os.path.abspath(os.path.join(BASE_DIR, "uploads", pdf_name))
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    pdf_text = extract_text_from_pdf(pdf_path)

    # the question-answering pipeline
    qa_model = pipeline("question-answering", model=model, tokenizer=tokenizer)
    
    # Processing the question using the question-answering pipeline
    response = qa_model(question=query_question, context=pdf_text)
    response_text = response['answer']

    return response_text
