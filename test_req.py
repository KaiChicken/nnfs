import requests
import json
url1 = "https://www.cocomanhua.com/"
url2 = "https://www.nvshens.org/img.html?img=https://img.onvshen.com:85/gallery/22359/23941/0.jpg"

r = requests.get(url1)
status = r.status_code
content = r.content
raw = r.raw

#result = r.json()

#jl = content.find(".jpg",0,-1)

print(type(content))
print(len(content))
print(content.decode)
print(len(r.text))

