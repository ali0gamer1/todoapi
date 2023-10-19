import requests
import string,random
endpoint = "http://127.0.0.1:8000/api/"

resp = requests.post(endpoint, json={"title":''.join([random.choice(string.ascii_letters) for a in range(10)]),
 "content":''.join([random.choice(string.ascii_letters) for a in range(10)]),
 "price":random.random()*10})

#resp = requests.put(endpoint, json={"title":"kiri", "content":"kiri", "price":1.1})
#resp = requests.delete(endpoint)
#resp = requests.get(endpoint)
print(resp.text)
