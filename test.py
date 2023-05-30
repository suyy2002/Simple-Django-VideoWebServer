import requests
import json

path = "uu53101798.yicp.fun/api"
url = "https://" + path + "/search/"

jsonData = {
    "keyword": "test",
    "search": "user",
    "page": 1,
}

r = requests.get(url, params=jsonData)
try:
    j = json.loads(r.text)
    print(j)
except:
    print(r.text)