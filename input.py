
ourChoices = {'add dish', 'delete dish', 'view dishes'}

prompt = '***  Dishes Application  ***\n' + 'add dish\n' + 'delete dish\n' + 'view dishes\n: '

userChoice = input(prompt).lower()


while userChoice not in ourChoices:
    # user_choice = input('Make the world go round?\n' +
    #                     'A little [default]\n' + 'Yes\n' + 'No').lower()
    userChoice = input('Tell me what shall i do ? \n'+
                       'add dish\n'
                       + 'delete dish\n'
                       + 'view dishes').lower()

# in case user didnt added any option : then by default it will ask the user to add the dish

user_choice = ourChoices[0] if not userChoice else userChoice
