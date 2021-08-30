#Data type----------------------------------------------#

# List 有順序，可動的列表
[3,4,5,"abc"]

# Tuple 有順序，不可動的列表
(3,4,5,6,7,"abc")

#Set 無順序
a={1,2,3,4,5}

print  (a)
#Data type----------------------------------------------#


#Data calculation----------------------------------------------#

#整數除法
print(3//6)
#小數除法
print (3/6)
#次方
print (2**5)
print (2**0.5)


#字串運算
s="Hello\" World"  #跳脫
s="Hello World"*3
print (s)
s= "Hello\nWorld"  #跟下面這行一樣
s= """Hello
World"""
print (s[2:]+s[:3])


#list運算
list_a = [1,2,3,4]
list_a[1:3]=[]  #連續刪除列表
list_a = list_a + [5,6]  #列表相加
print (list_a)
#巢狀烈表
list_a = [[1,2,3],[4,5,6]]
print (list_a)
#list_a[0][0] = [5,5,5]  #指定只能變成插入新列表
list_a[0][0:2] = [5,5,5] #指定範圍才才能使用插入列表
print (list_a)
#tuple 運算都跟list一樣，但tuple是不能變動的


#集合的運篹
set1 = {1,2,3}
#print (3 in set1) # in / not in
set2 = {3,4,5}
#print(set2&set1) #交集
#print(set2|set1) #聯集，但不重複取
#print(set2-set1) #差集
#print(set2^set1) #反交集
#print ("a" in set("apple"))#set("字串")


#字典運算
dic = {1:"abc","2":"bcd"} #key value pair
print (1 not in dic)  # 判斷key 是否存在
print ("b" in dic["2"]) #判斷value
del dic[1] # 刪除key
print(dic)

dic ={x:x*2 for x in [3,4,5]} #以列表資料當基礎，產生字典



#Data calculation----------------------------------------------#


#函式練習-----------------------------------------#
#def print_(a=5):  #參數給預設值
#    print (a)
#print(print_())

#無限參數 使用tuple方式處理
def say(*msgs):
    for msg in msgs:
        print(msg)
say([123],{1,2,3,4},"1321")



#函式練習-----------------------------------------#


#mudule練習---------------------------------------#
import sys as s
#print (s.path)
s.path.append("modules") # 將自己的modules放到特定資料夾，但需要先將path載入
#mudule練習---------------------------------------#

#專案檔案配置----------------------------------------------#
#封包資料夾，必須包含__init__.py檔案
import modules.point
#print (modules.point.distance(3,4))

#專案檔案配置----------------------------------------------#


#檔案操作-----------------------------#
# 模式: 讀取:r 寫入:w 讀寫: r+
#file = open("data.txt",mode="w",encoding="utf-8")
#file.write("測試中文")
#file.close()
# 精簡寫法 (不需要關閉)
sum = 0
with open("data.txt",mode="w",encoding="utf-8") as file:
    file.write("5\n6")
with open("data.txt",mode="r",encoding="utf-8") as file:
    for line in file:  #same as readline to string
       print (type(line)) 
    lines = file.read()  # read size or read all to string
    #line = file.readline() # read one line to string
    #lines = file.readlines() #read all to list
#print(line)
#print (lines)
#print (sum)
#檔案操作-----------------------------#


#json練習--------------------------------#
import json

#讀取json資料#
with open("config.json",mode="r") as file:
    data = json.load(file)
#print (data) #data是一個字典
#print ("Name: "+data["name"])
#print ("Name:",data["name"])
data["name"] ="John"
with open("config.json",mode="w") as file:
    json.dump(data,file)
#print (data)
#json練習----------------------------------------------#

#隨機選取-----------------------------------------------#
import random



print (random.random()) #0.0~1.0之間的隨機亂數 = random.uniform(0.0,1.0)
print (random.sample([1,2,3,4,5],3)) #取隨機三個
list=[1,3,5,4,5]
random.shuffle(list) #random.shuffle返回值為null，並非shuffle後的結果
print (list) 
print (random.uniform(1,4)) #亂數隨機取得1~4
print (random.normalvariate(100,10))#平均數=100 標準差=10，常態非配亂數，得到的資料多數在90~110之間

#統計模組
import statistics as stat
print (stat.mean([1,2,3,4,5,100])) #平均數
print (stat.median([1,2,3,3,4,5,100])) #中位數
print (stat.stdev([1,2,3,4,5,100])) #標準差
#隨機選取-----------------------------------------------#


#類別練習---------------------------------------------#
import ClassTest as ph

print (ph.Name("klcheng","Chen").firstName)
print (ph.Name("klcheng","Chen").lastName)
ph.Phone("ios","8",False).showInfo()

file1 = ph.OpenFile("data.txt")
file1.open()
print(file1.read())

#print (ph.OpenFile("data.txt").open())

#類別練習---------------------------------------------#
