from data_processing.file_reader import read_data
from data_processing.web_fetcher import fetch_user_data

file_data = read_data("data.txt")
usernames = fetch_user_data()

print("Data from file:")
print(file_data)

print("\nUsernames from API:")
print(usernames)