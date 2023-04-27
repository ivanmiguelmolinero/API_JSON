import requests

if __name__ == "__main__":

    url = "https://api.publicapis.org/entries"

    # A GET request to the API
    response = requests.get(url)

    # Print the response
    response_json = response.json()
    print(response_json)

    print(type(response_json))