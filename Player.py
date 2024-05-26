#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class player:
    def __init__(self, money = 70000, po = 0):
        self.__money = money
        self.__po = po

    def setName(self, name):
        self.__name = name
        
    def getName(self):
        return self.__name

    def setMoney(self, add):
        self.__money += add
        
    def getMoney(self):
        return self.__money

    def setPo(self, move):
        self.__po += move
        
    def getPo(self):
        return self.__po


# In[ ]:




