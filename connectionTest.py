#網路連線
import urllib.request as request

src = "https://www.ntu.edu.tw/"

with request.urlopen(src) as response:
    data=response.read().decode("utf-8")
#print (data)

#讀取json檔案
import json
with open("臺北內湖科技園區廠商名錄.json",mode="r",encoding="utf-8") as file:

    data = json.load(file)

for row in range(0,len(data)):
    print (data[row]["公司名稱"])
