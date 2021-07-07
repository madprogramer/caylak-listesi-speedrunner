import requests,json; 
with open("cookies.json",'r') as cookies:
  with open("headers.json",'r') as headers:
    r=requests.get("https://eksisozluk.com/",cookies=json.loads(cookies.read()),headers=json.loads(headers.read()))
    #r=requests.get("https://eksisozluk.com/")
    print(r)