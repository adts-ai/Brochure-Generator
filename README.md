# Brochure Generator with OpenAI API 🌍📄

## A Python Tool to Create Brochures from Websites 🚀💡

The **Brochure Generator** is a Python-based tool that scrapes relevant content from any website and uses the power of OpenAI’s GPT model to generate a polished brochure. It extracts company info, career opportunities, and other valuable details while filtering out unnecessary links like privacy policies. The final brochure is displayed in an engaging, readable format such as **Markdown**.

![Brochure Generator](./visuals/brochure_generator_visual.png)  <!-- Optional image path -->

## Features

✨ **Key Features**:
- **Scrapes websites** and extracts only relevant content like company info, about pages, and careers.
- **Uses OpenAI's GPT model** to generate a concise, engaging brochure from the scraped content.
- **Multiple output formats** supported, with **Markdown** as the default.
- **Simple to use**: Just provide any website URL, and the tool generates a professional brochure in seconds.

## Requirements

To use the **Brochure Generator**, ensure you have the following:

- **Python 3.x**
- **requests**: To retrieve webpage content.
- **BeautifulSoup**: For parsing HTML and cleaning the website content.
- **openai**: To interact with OpenAI’s GPT model.
- **python-dotenv**: To securely manage API keys and environment variables.
- **IPython**: For displaying the summary in Markdown (optional, especially for Jupyter environments).

Install the required libraries using pip:

```bash
pip install requests beautifulsoup4 openai python-dotenv ipython
```

## Usage
Initialization
First, create a `.env` file and provide your OpenAI API credentials as shown below:

```env
OPENAI_API_AZURE_KEY=your_openai_api_key_here
AZURE_OPENAI_ENDPOINT=https://your_endpoint_url_here
OPENAI_AZURE_MODEL=gpt-4o-mini
```

## Generating a Brochure
To generate a brochure for a website, simply call the `BrochureGenerator.generate()` method with the company name and website URL:

```python
BrochureGenerator.generate("HuggingFace", "https://huggingface.co")
```

This will:

1. Scrape the website content.

2. Use OpenAI’s GPT model to generate a polished brochure.

3. Display the result in the specified format (Markdown).

## Customizing
You can customize the generated brochure by modifying the scraping and content formatting options in the code. For example, you can adjust the model or change the content structure as needed.

```python
BrochureGenerator.generate("My Company", "https://example.com")
```

## How it Works 🔍
1. Website Scraping: The `Website` class extracts the title, text, and links from the provided URL. It filters out unnecessary links and keeps only the relevant ones (e.g., About, Careers).

2. Link Filtering: The system processes the extracted links, removing irrelevant ones like Terms of Service, Privacy Policy, etc., and identifies key links to be included in the brochure.

3. AI Brochure Creation: Using OpenAI’s GPT model, the `BrochureGenerator` class generates a professional brochure, making the information engaging and clear.

4. Display Summary: The brochure content is returned and displayed in an easy-to-read format (e.g., Markdown).

## Example Code

```python
BrochureGenerator.generate("HuggingFace", "https://huggingface.co")
```

This will automatically fetch the company information, generate a brochure, and display it in the Markdown format.

## Contribution 🤝
Feel free to fork this repository, submit issues, or contribute by making pull requests to improve the project! We welcome your contributions to make the Brochure Generator even better.