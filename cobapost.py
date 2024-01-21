import requests
# jika pake request post yang diakses log elif POST di main,py
mydata={"nama":"wandu"}
req=requests.post("http://127.0.0.1:5000/cobarequest", data=mydata)

print(req.text)