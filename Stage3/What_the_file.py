import requests

def the_file(url):
    response = requests.get(url)

    if response.status_code == 200:
        with open('source.html', 'wb') as file:
            file.write(response.content)
            print("Content saved.")
    else:
        print(f"The URL returned {response.status_code}.")

# Get URL from user input
url = input("Please enter the URL: ")

# Call the function to save the page source
the_file(url)
