# NeoGen - Smart Product Copy Generator

This tool generates e-commerce product titles, descriptions, and SEO keywords using OpenAI GPT-4 and Vision API, powered by data from Google Sheets.

## Features
- Image-based product understanding
- Multilingual (Arabic + English)
- Google Sheets integration
- Auto-populated title, short & long descriptions, and SEO

## Setup

1. **Install Dependencies**
```bash
pip install openai gspread oauth2client python-dotenv
```

2. **Setup Environment**
- Create a `.env` file based on `.env.example`
- Get your OpenAI API Key
- Create a Google Cloud service account and get the JSON key
- Share your Google Sheet with the service account email

3. **Run the Script**
```bash
python google_sheets_generator.py
```

Make sure your sheet has the following columns:
- Category, Brand, Attributes, Image URL, Language, Tone, Title, Short Description, Long Description, SEO Keywords

## Coming Soon
- Streamlit Web App
- File Upload & Excel Export
- Tone Control, Language Selector, UI Dashboard