class Menu:

    def __init__(self):
        self.meals = []

    #===== write your code below =======
    def add_meal(self, meal):
        self.meal = meal
        self.meals.append(self.meal)
    def print_menu(self):
        for i in range(len(self.meals)):
            print(self.meals[i])
    def get_meal(self, idx):
        self.idx = idx
        try:
            print(self.meals[self.idx])
        except TypeError:
            print('Index should be an integer.')
        except IndexError:
            print('This meal does not exist.')
    def clear_menu(self):
        self.meals.clear()
    
if __name__ == '__main__':
    menu = Menu()
