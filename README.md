# ✨ Brochure Generator with OpenAI API 🚀

Are you looking to automate the process of creating professional brochures from websites? This Python-powered Brochure Generator is here to save you time and effort by scraping valuable content from websites and transforming it into a well-crafted brochure. Powered by OpenAI’s GPT model, this project filters through web content to extract only the most relevant information and presents it in a polished, shareable format. Perfect for businesses, content creators, and digital marketers looking to streamline their marketing materials!

## 🚀 Key Features

- **Smart Web Scraping**: Automatically grabs relevant data from websites like company overviews, careers, and more.
- **AI-Powered Brochure Creation**: Uses OpenAI to craft engaging and concise brochures from raw website data.
- **Customizable & Scalable**: Easily adaptable to other use cases—just provide any website URL and let the magic happen.
- **Save Time**: Cut down on hours spent manually creating marketing materials by automating the process with AI.

## 🔧 Requirements

Before you get started, make sure you have the following:

- **Python 3.6+**
- Libraries:
  - `requests`
  - `beautifulsoup4`
  - `openai`
  - `python-dotenv`
  - `IPython`

Install them with this single command:

```bash
pip install requests beautifulsoup4 openai python-dotenv ipython

##⚙️ Setup Guide
Create a .env file in the root of the project.

Add your OpenAI API credentials by including the following variables in your .env file:

OPENAI_API_AZURE_KEY: Your OpenAI Azure API Key

AZURE_OPENAI_ENDPOINT: Your OpenAI API Endpoint URL

OPENAI_AZURE_MODEL: Model ID (e.g., gpt-3.5-turbo)

Example .env file:
