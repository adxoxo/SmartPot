import requests

url = "http:192.168.1.67:8000/api/data/tempread/"

response = requests.get(url)

csrftoken = response.cookies['csrftoken']

print(csrftoken)