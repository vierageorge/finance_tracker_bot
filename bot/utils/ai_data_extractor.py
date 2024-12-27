from openai import OpenAI
from dotenv import load_dotenv
from utils.api import get_categories
import json
load_dotenv()

client = OpenAI()

system_prompt = '''
    You are an agent specialized in extracting information from images of bank money transfers.
    You will be provided with an image and the caption of the image that describes the purpose of the money transfer, and your goal is to extract the numeric amount of the money transfer, and to categorize the money transfer. 
    The amount should be extracted as an integer, and the category should be extracted as a string.
    You should return the category that best describes the money transfer. You will only use the categories provided, and you should not return a category that is not in the list.
    Return format will be a json object with the following structure:
    {
        "amount": 1000,
        "category": "furniture"
    }
    No additional information should be returned, just the json object. Do not include the markdown text. This json object will be parsed by the system to extract the amount and the category, so only include in the response the json object that can be parsed successfully.
    The possible categories are: 
'''

def analyze_image(img_url: str, caption: str) -> dict:
    categories = get_categories()
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": system_prompt + ', '.join(categories)
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": img_url,
                    }
                },
            ],
        },
        {
            "role": "user",
            "content": caption
        }
    ],
        max_tokens=300,
        top_p=0.1
    )
    content = response.choices[0].message.content
    return json.loads(content) if content else {}