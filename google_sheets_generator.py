import os
import openai
import gspread
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(os.getenv("SERVICE_ACCOUNT_JSON_PATH"), scope)
client = gspread.authorize(creds)
sheet = client.open_by_key(os.getenv("GOOGLE_SHEET_ID")).sheet1

def generate_copy(category, brand, attributes, language, tone, image_url=None):
    messages = [
        {"role": "user", "content": [
            {"type": "text", "text": "Generate a product title, short description, long description, and SEO keywords based on the image and details below."},
            {"type": "image_url", "image_url": {"url": image_url}} if image_url else {},
            {"type": "text", "text": f"Category: {category}
Brand: {brand}
Attributes: {attributes}
Language: {language}
Tone: {tone}"}
        ]}
    ]

    # Remove empty dict if no image
    messages[0]["content"] = [msg for msg in messages[0]["content"] if msg]

    response = openai.ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=messages,
        temperature=0.7,
        max_tokens=600
    )
    return response['choices'][0]['message']['content']

# Read rows and generate output
rows = sheet.get_all_values()[1:]
for i, row in enumerate(rows, start=2):
    category, brand, attributes, image_url, language, tone = row[:6]
    if not row[6]:  # Skip if already processed
        result = generate_copy(category, brand, attributes, language, tone, image_url)
        output_lines = result.split('\n')
        for j, value in enumerate(output_lines[:4]):  # Fill Title, Short Desc, Long Desc, SEO
            sheet.update_cell(i, 7 + j, value.replace("Title: ", "").replace("Short Description: ", "").replace("Long Description: ", "").replace("SEO Keywords: ", ""))