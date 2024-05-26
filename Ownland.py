class ownland:
    def __init__(self, name="ownland", money1=0, owner1=0, owner2=0, money2=0, tolls1=0, tolls2=0, estate1=0, estate2=0):
        self.__name = name
        self.__money1 = money1
        self.__owner1 = owner1
        self.__owner2 = owner2
        self.__money2 = money2
        self.__tolls1 = tolls1
        self.__tolls2 = tolls2
        self.__estate1 = estate1
        self.__estate2 = estate2

    def setName(self, name):
        self.__name = name
        
    def getName(self):
        return self.__name
    
    def setMoney1(self, money1):
        self.__money1 = money1
        
    def getMoney1(self):
        return self.__money1
    
    def setMoney2(self, money2):
        self.__money2 = money2
        
    def getMoney2(self):
        return self.__money2

    def setOwner1(self, owner1):
        self.__owner1 = owner1
        
    def getOwner1(self):
        return self.__owner1
    
    def setOwner2(self, owner2):
        self.__owner2 = owner2
        
    def getOwner2(self):
        return self.__owner2
    
    def setpay1(self, tolls1):
        self.__tolls1 = tolls1
        
    def getpay1(self):
        return self.__tolls1
    
    def setpay2(self, tolls2):
        self.__tolls2 = tolls2
        
    def getpay2(self):
        return self.__tolls2
    
    def setestate1(self, estate1):
        self.__estate1 = estate1
        
    def getestate1(self):
        return self.__estate1
    
    def setestate2(self, estate2):
        self.__estate2 = estate2
        
    def getestate2(self):
        return self.__estate2