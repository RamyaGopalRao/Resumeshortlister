from openai import OpenAI
from PyPDF2 import PdfReader
import json
from django.conf import settings
from .models import Education,Resume,Experience

# Initialize OpenAI API



def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text


def parse_resume(file_path,user_message):
    client = OpenAI(
        api_key="******"    )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": user_message}
        ]
    )

    bottext = completion.choices[0].message.content.strip()
    trimmed_str = bottext.replace('```json\n', '').replace('```', '')
    print(trimmed_str)
    resume_dict=json.loads(trimmed_str.strip())
    return resume_dict



