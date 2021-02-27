import sys
from .DishHandler import DishHandler
from .inputHandler import inputHandler


def main():
    """
    handles the input and performs the necessary taks, required
    :return:
    """
    i = inputHandler()

    pg = DishHandler()

    while True:

        userChoice, name,indegrents = i.input()

        if userChoice == 1 and name is not None and indegrents is not None:

            pg.addDish(name,indegrents)

        elif userChoice == 2 and name is not None:

            pg.deleteDish(name)

        elif userChoice == 3 and name == -1:

            pg.viewAllDishes()

        elif userChoice == 4 and name == None and indegrents is not None:

            s = pg.dishesCanBeMAde(indegrents)
            pg.viewDishesHelper(s)

        elif userChoice == -1 and name == -1:

            print('*' * 50)

            print('Exiting the application')

            print('*'*50)

            break

        else:

            # default -> Not valid choices

            print('Not valid choices')


if __name__ == '__main__':
    main()