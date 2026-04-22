from interact import gHealth
from data import record, retrieve
from datetime import datetime
class API(gHealth):
    def __init__(self, name, age, gender, height):
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
# main execution
health1 = API("Razak Mohamed",34,"male",158)
health1.makeWeighIn(id=1,weight=71.02)
print(health1.readWeighIn("1"))
print(health1.updateWeighIn(id=1,weight=65))