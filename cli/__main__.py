import sys
from .DishHandler import DishHandler
from .inputHandler import inputHandler


def main():

    i = inputHandler()

    pg = DishHandler()

    while True:

        userChoice, name = i.input()

        if userChoice == 'add dish' and name is not None:

            pg.addDish(name)

        elif userChoice == 'delete dish' and name is not None:

            pg.deleteDish(name)

        elif userChoice == 'view dishes' and name is None:

            pg.viewAllDishes()

        elif userChoice == '-1' or name == '-1':

            print('*' * 50)

            print('Exiting the application')

            print('*'*50)

            break

        else:

            # default -> Not valid choices

            print('Not valid choices')


if __name__ == '__main__':
    main()