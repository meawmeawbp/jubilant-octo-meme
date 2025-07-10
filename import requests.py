import requests

url = "https://sth.sh"
r = requests.get(url)

print("Status:", r.status_code)
print("Headers:", r.headers)
print("Body:", r.text)
