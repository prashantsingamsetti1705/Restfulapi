import requests
Base_url="http://127.0.0.1:8000/"
End_url="apiclassbased/"
resp=requests.get(Base_url+End_url)
data=resp.json()
print('datafrom put method')