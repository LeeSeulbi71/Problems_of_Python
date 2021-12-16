
class Menu:

    def __init__(self):
        self.meals = []

    #===== write your code below =======
    def add_meal(self, meal):
        self.meal = meal
        self.meals.append(meal)
    def print_menu(self):
        for meal in self.meals:
            print(meal)
    def get_meal(self, idx):
        self.idx = idx
        try:
            print(self.meals[idx])
        except TypeError:
            print('Index should be an integer.')
        except IndexError:
            print('This meal does not exist.')
    def clear_menu(self):
        self.meals.clear()



if __name__ == '__main__':

    menu = Menu()
    menu.add_meal("Burger")
    menu.add_meal("Pizza")
    menu.add_meal("Chicken")
    menu.print_menu()
    menu.get_meal(1)
    menu.get_meal("Burger")
    menu.get_meal(5)
    menu.get_meal(0.8)
    menu.clear_menu()
    print(menu)