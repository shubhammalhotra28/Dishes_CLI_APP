# import Dish

'''

Assumptions for class Dish :
    1) Each Dish will be having a valid name
'''

class Dish:

    def __init__(self,name):
        self.name = name

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


    def viewAllDishes(self):

        for i in self.dict:
            print(i,' ','primary_key = ',self.dict[i])


    def deleteDish(self,name):

        if name not in self.dict:
            print('dish name does not exist')
            return -1

        del self.dict[name]
        self.primary_key -= 1

s = Solution()
s.addDish('fish')
s.addDish('chicken')
s.addDish('rajma chawal')
print('*'*78)
s.viewAllDishes()
s.deleteDish('rajma chawal')
print('*'*78)
s.viewAllDishes()
s.addDish('chicken')
print('*'*78)
s.viewAllDishes()
s.deleteDish('rajma chawal')
s.viewAllDishes()
print('*'*78)

