
from .Dish import Dish

'''
Assumptions for Solution :
    1) we will be storing all the values within the hashmap and at intiailisation of this class
        a disctionary and an integer (primary_key) will be intialised 
'''

class DishHandler:

    def __init__(self):

        self.dict = {} #map
        self.count = 0 # acts like a pk

    def addDish(self,name,indegrents):
        """
        adds dish if not present else prints a message
        :param name: string
        :return: None
        """
        if name in self.dict:
            print('dish already exist')
            return -1

        # add indegrients

        dish = Dish(name, self.count,indegrents)
        self.dict[name] = dish
        self.count += 1
        print(name,' dish added successfully')
        return


    def viewAllDishes(self):

        """
        view all dishes within the hashmap along with the primary key values
        :return: None
        """

        print('*'*50)
        print('The list of dishes are as followed:')
        print('*'*50)

        for i in self.dict:
            print(i,' ','primary_key = ',self.dict[i].id,self.dict[i].indegrents)

        return

    def deleteDish(self,name):
        """
        delete the dish fron the map if present else return -1
        :param name: string
        :return: None
        """

        if name not in self.dict:
            print('dish name does not exist')
            return -1

        del self.dict[name]
        print(name,' dish removed successfully')

    def dishesCanBeMAde(self,indegrents):

        a = {}
        for i in indegrents:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1

        indegrents = a
        s = set()
        for dish in self.dict:
            count = 0
            indegrentsCount = len(indegrents)
            # print('dish',dish)

            li = self.dict[dish].indegrents # list
            # print(li)
            for ind in li:
                if ind in indegrents:
                    count += 1
            if count <= indegrentsCount:
                # add it within some ds and return it
                s.add(dish)

        return s
        ''' a : -> b c d
        ->check  = b c d e
        
        
        '''

        ''''
        tomatoes
        '''


    def viewDishesHelper(self,s):

        for i in s:

            print(i)
        return
