from abc import *
class gHealth:
    @abstractmethod
    def makeWeighIn(self,**kwargs): pass
    @abstractmethod
    def updateWeighIn(self,id,**kwargs):pass
    @abstractmethod
    def readWeighIn(self,id):pass
    @abstractmethod
    def calculateMetrics(self,weight):pass