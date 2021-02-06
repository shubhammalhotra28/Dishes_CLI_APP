
class inputHandler:

    def input(self):

        ourChoices = {'add dish', 'delete dish', 'view dishes','-1'}

        prompt = '***  Dishes Application  ***\n' + 'add dish\n' + 'delete dish\n' + 'view dishes\n: '

        userChoice = input(prompt).lower()


        while userChoice not in ourChoices:
            userChoice = input('Tell me what shall i do ? \n'+
                               'add dish\n'
                               + 'delete dish\n'
                               + 'view dishes').lower()

        userChoice = ourChoices[0] if not userChoice else userChoice

        name = None

        if userChoice in ('add dish', 'delete dish'):

            print('Enter the valid name of the dish')
            name = input().lower()

        elif userChoice in ('view dishes'):
            name = None


        return userChoice,name
