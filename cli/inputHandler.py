"""

Class : respnsible to handle the input
"""


class inputHandler:

    def input(self):
        """
            Function handling the input, 1: to add dish, 2: delete dish, 3: view dishes, -1: exit
            Returns a tuple of userChoice along with the name of the dish
        :return: (userChoice,name)
        """
        ourChoices = {1, 2, 3,-1,4}

        prompt = '***  Dishes Application  ***\n' + 'Press 1 to add dish\n' + 'Press 2 to delete dish\n' + 'Press 3 to view dishes\n: '+'Press -1 to delete dish\n'

        userChoice = int(input(prompt))


        while userChoice not in ourChoices:
            userChoice = int(input('Tell me what shall i do ? \n'+
                               'Press 1 to add dish\n'
                               + 'Press 2 to delete dish\n'
                               + 'Press 3 to view dishes\n'
                               +  'Press -1 to delete dish\n'))

        userChoice = ourChoices[0] if not userChoice else userChoice

        name = None
        indegrents = None
        if userChoice == 1:

            print('Enter the valid name of the dish')
            name = input().lower()

            while len(name)==0:
                print('Enter the valid name of the dish')
                name = input().lower()

            print('Enter indegrients of : ', name)
            indegrents = input().strip().split()

        elif userChoice == 2:


            print('Enter the valid name of the dish')
            name = input().lower()

            while len(name)==0:
                print('Enter the valid name of the dish')
                name = input().lower()

        elif userChoice == 4:
            # u will be giving the indegrints
            print('Enter indegrients of : ')
            indegrents = [s for s in input().strip().split()]
            # indegrents = input().strip().split()


        elif userChoice == 3:
            name = -1
        elif userChoice == -1:
            userChoice = -1
            name = -1

        return userChoice,name,indegrents
