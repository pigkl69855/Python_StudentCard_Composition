
class Date:
    def __init__(self,month,day,year):
        self.__month = month
        self.__day = day
        self.__year = year
    
        
    def getYear(self):
        return self.__year
    def getMonth(self):
        return self.__month
    def getDay(self):
        return self.__day

    def setYear(self,year):
        self.__year = year
    def setMonth(self,month):
        self.__month = month
    def setDay(self,day):
        self.__day = day

    def toString(self):
        print(self.__month,'\\',self.__day,'\\',self.__year, end = '')

