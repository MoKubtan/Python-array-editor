from icecream import ic
cars=[]
def menu():
    while(True):
        ic('a - add your car')
        ic('p - print all cars')
        ic('x - exit')
        user_selection = input("select a menu option")
        if user_selection == 'a':pass
        if user_selection == 'p':ic(cars)
        if user_selection == 'x':exit()
menu()