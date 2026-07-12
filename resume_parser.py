# resume_parser.py
# This file reads a resume file and returns its text.

import os

import PyPDF2
from docx import Document


def extract_text_from_pdf(file_path):
    """Read text from a PDF resume."""
    text = ""

    with open(file_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        for page in pdf_reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text.strip()


def extract_text_from_docx(file_path):
    """Read text from a DOCX resume."""
    document = Document(file_path)
    paragraphs = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            paragraphs.append(paragraph.text)

    return "\n".join(paragraphs)


def extract_text(file_path):
    """Check the file type and call the correct function."""
    if not os.path.exists(file_path):
        raise FileNotFoundError("Resume file was not found.")

    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == ".pdf":
        return extract_text_from_pdf(file_path)

    if file_extension == ".docx":
        return extract_text_from_docx(file_path)

    raise ValueError("Only PDF and DOCX resume files are supported.")
