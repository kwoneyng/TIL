import requests,json
myans = {
    "nickname":"서울 2반 박권응",
    "yourAnswer":"Kubernetes"
}
headers = {
    "Accept":"application/json", 
    "Content-Type":"application/json"
}
print(headers['Accept'])
r = requests.post("http://13.125.222.176/quiz/jordan", data=json.dumps(myans), headers=headers)
# print(r.status_code)
# print(r.headers)
print(r.json())