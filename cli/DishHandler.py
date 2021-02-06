
from .Dish import Dish

'''
Assumptions for Solution :
    1) we will be storing all the values within the hashmap and at intiailisation of this class
        a disctionary and an integer (primary_key) will be intialised 
'''

class Solution:

    def __init__(self):

        self.dict = {}
        self.primary_key = 0

    def addDish(self,name):
        if name in self.dict:
            print('dish already exist')
            return -1

        dish = Dish(name)
        self.primary_key += 1
        self.dict[name] = self.primary_key
        print(name,' dish added successfully')
        return


    def viewAllDishes(self):

        print('*'*50)
        print('The list of dishes are as followed:')
        print('*'*50)

        for i in self.dict:
            print(i,' ','primary_key = ',self.dict[i])

        return

    def deleteDish(self,name):



        if name not in self.dict:
            print('dish name does not exist')
            return -1

        del self.dict[name]
        self.primary_key -= 1
        print(name,' dish removed successfully')

