
class Phone:

    def __init__(self,os,number,is_waterproof): # 初始化函式
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof


    def showInfo(self):
        
        print (self.os)
        print (self.number)
        print (self.is_waterproof)
        
        return 0

class Name:
    def __init__(self,firstName,LastName):
        self.firstName = firstName
        self.lastName = LastName
class OpenFile:
    def __init__(self,name):
        self.name=name
        self.file=None

    def open(self):
        self.file=open(self.name,mode="r",encoding="utf-8")

    def read(self):
        return self.file.read()

