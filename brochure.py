import os
import requests
import json
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import openai
from IPython.display import Markdown, display, update_display

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_AZURE_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
headers = {"User-Agent": "Mozilla/5.0"}

link_system_prompt = """
You are provided with links found on a webpage. Decide which links are relevant for a brochure, like About, Careers, etc.
Respond in JSON:
{
    "links": [{"type": "about", "url": "https://example.com/about"}]
}
"""

class Website:
    def __init__(self, url):
        self.url = url
        self.scrape()

    def scrape(self):
        soup = BeautifulSoup(requests.get(self.url, headers=headers).content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title"
        self.text = soup.get_text(separator="\n", strip=True)
        # Filter out non-http(s) links
        self.links = [link.get('href') for link in soup.find_all('a') if link.get('href') and link.get('href').startswith(('http', 'https'))]

    def get_contents(self):
        return f"Title:\n{self.title}\nContents:\n{self.text}"

class BrochureGenerator:
    @staticmethod
    def get_links(website):
        prompt = f"Here are the links on {website.url} - decide which are relevant for a brochure. Do not include Terms, Privacy.\n" + "\n".join(website.links)
        response = openai.chat.completions.create(
            model=os.getenv("OPENAI_AZURE_MODEL"),
            messages=[{"role": "system", "content": link_system_prompt}, {"role": "user", "content": prompt}],
            temperature=0.7
        )
        return json.loads(response.choices[0].message.content.strip("```json\n").strip("```"))

    @staticmethod
    def get_brochure(user_prompt):
        response = openai.chat.completions.create(
            model=os.getenv("OPENAI_AZURE_MODEL"),
            messages=[{"role": "system", "content": "Create a brochure from the provided info."}, {"role": "user", "content": user_prompt}]
        )
        display(Markdown(response.choices[0].message.content))

    @staticmethod
    def generate(company_name, url):
        website = Website(url)
        user_prompt = f"Company: {company_name}\n" + website.get_contents()
        links = BrochureGenerator.get_links(website)
        for link in links["links"]:
            user_prompt += f"\n{link['type']} - {Website(link['url']).get_contents()}"
        user_prompt = user_prompt[:5000]  # Limit prompt size
        BrochureGenerator.get_brochure(user_prompt)

# Example usage
BrochureGenerator.generate("HuggingFace", "https://huggingface.co")