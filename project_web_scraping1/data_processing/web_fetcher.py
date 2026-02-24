import requests

def fetch_user_data():
    store_data= []
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    raw_data = response.json()
    for data in raw_data:
        extracted_username = data["username"]
        store_data.append(extracted_username)
    return store_data

