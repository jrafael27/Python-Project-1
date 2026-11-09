import requests

url = "https://api.github.com/users/octocat"
res = requests.get(url, timeout=10)

print(res.status_code)
data = res.json()
print(data["login"], data["public_repos"])

try:
    res = requests.get(url, timeout=10)
    res.raise_for_status()  # Raise an exception for HTTP errors
except requests.exceptions.RequestException as e:
    print("Gagal: ", e)
    
res = requests.post("https://httpbin.org/post", json={"halo": "dunia"}, timeout = 10)

print(res.json())