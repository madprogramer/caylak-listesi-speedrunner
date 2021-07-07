import requests,json,os,sys;

PATH = os.path.dirname(sys.argv[0])
with open(os.path.join(PATH,"cookies.json"),'r') as cookies:
  with open(os.path.join(PATH,"headers.json"),'r') as headers:
    r=requests.get("https://eksisozluk.com/",cookies=json.loads(cookies.read()),headers=json.loads(headers.read()))
    #r=requests.get("https://eksisozluk.com/")
    print(r)