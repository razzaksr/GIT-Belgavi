from data import record, retrieve
from datetime import datetime
from abc import *
# Abstract with factory pattern
class gHealth:
    @staticmethod
    def getHealth():
        return API()
    @abstractmethod
    def makeWeighIn(self,**kwargs): pass
    @abstractmethod
    def updateWeighIn(self,id,**kwargs):pass
    @abstractmethod
    def readWeighIn(self,id):pass
    @abstractmethod
    def calculateMetrics(self,weight):pass
    @abstractmethod
    def filter(self,criteria,value,operate):pass
class API(gHealth):
    def __init__(self, name="", age=0, gender="", height=0):
        self.__name = name
        self.__age=age
        self.__gender=gender
        self.__height = height
    def initialize(self,name="", age=0, gender="", height=0):
        self.__name = name
        self.__age=age
        self.__gender=gender
        self.__height = height
        
    # bmi, bmr, muscle rate, fat rate, body age
    def calculateMetrics(self,weight):
        bmi = round(weight/(self.__height/100)**2,1)
        if self.__gender == "male": 
            bmr = 10*weight+6.25*self.__height-5*self.__age+5
        else:
            bmr = 10*weight+6.25*self.__height-5*self.__age-161
        bodyAge = self.__age+(2 if bmi<18.5 else 5 if bmi>25 else 0)
        fatRate = round((1.20*bmi)+(0.23*self.__age)-
        (16.2 if self.__gender=="male" else 5.4),1)
        muscleRate = round(weight-(fatRate/100)*weight,1)
        return {
            "bmi":bmi,"bmr":bmr,"fat-rate":fatRate,"muscle-rate":muscleRate,
            "body-age":bodyAge
        }
    def readWeighIn(self, id):
        collected = retrieve()
        return collected.get(id,"Weight-IN id not available")
    def makeWeighIn(self, **kwargs):
        collected = retrieve()
        weId = int(kwargs.get("id"))
        weight = kwargs.get("weight")
        metrics = self.calculateMetrics(weight)
        trend = {
            "name":self.__name,
            "age":self.__age,
            "gender":self.__gender,
            "date":datetime.now().strftime("%Y-%m-%d %H:%M"),
            "weight":weight,**metrics
        }
        collected[weId]=trend
        record(collected)
        return "Weigh-In "+str(weId)+" recorded"
    def updateWeighIn(self, id, **kwargs):
        collected = retrieve()
        weId = str(id)
        if weId in collected:
            weight = kwargs.get("weight",collected[weId]["weight"])
            metrics = self.calculateMetrics(weight)
            collected[weId].update({
                "name":self.__name, "age":self.__age,"gender":self.__gender,
                "weight":weight,
                "date":datetime.now().strftime("%Y-%m-%d %H:%M"),
                **metrics,
            })
            record(collected)
            return "Weigh_In updated"
        else: return "WeighIn-Id not found"
    @staticmethod
    def filter(criteria, value, operate):
        collected = retrieve()
        result = []
        for each in collected.values():
            if operate == "eq" and each[criteria]==value:
                result.append(each)
            elif operate == "le" and each[criteria]<=value:
                result.append(each)
            elif operate == "ge" and each[criteria]>=value:
                result.append(each)
            elif operate == "ne" and each[criteria]!=value:
                result.append(each)
        return result