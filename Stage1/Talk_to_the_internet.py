import requests
import json

def get_quote_from_url(url):
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = json.loads(response.text)
            quote = data.get('content')
            if quote:
                return quote
            else:
                return "Invalid quote resource!"
        except json.JSONDecodeError:
            return "Invalid JSON response!"
    else:
        return "Invalid quote resource!"

# Get URL from user input
url = input()

# Call the function and print the result
quote_result = get_quote_from_url(url)
print(quote_result)
