import requests
import json


api_key="xxxxxxxx"
api_url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_döviz=input("bozulan döviz türü:")
alınan_döviz=input("Alınan döviz kuru")
miktar=float(input(f"ne kadar {bozulan_döviz} bozdurmak istiyorsunuz?"))

sonuc=requests.get(api_url+bozulan_döviz)
sonuc_json=json.loads(sonuc.text)
kur=float(sonuc_json["conversion_rates"][alınan_döviz])
print(kur*miktar)