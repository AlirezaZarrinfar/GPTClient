import openai
from django.conf import settings

openai.api_key = settings.APIKEY

def send_code_to_api(code):
    try:
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": code}],
        )
        return res["choices"][0]["message"]["content"]
    except openai.error.APIError as e:
        raise ValueError(f"OpenAI API returned an API Error: {e}")
    except openai.error.APIConnectionError as e:
        raise ValueError(f"Failed to connect to OpenAI API: {e}")
    except openai.error.RateLimitError as e:
        raise ValueError(f"OpenAI API request exceeded rate limit: {e}")



# def send_code_to_api(code):
#     from api import mock_data
#     return mock_data.json_data[code.replace("\"", "'")]