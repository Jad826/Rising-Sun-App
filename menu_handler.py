
import Register_Login

def menu():
    menu = int(input("Welcome to the python client test Login Register! Choose your option \n 1.Register \n 2.Login \n 3.Exit \n What do you want?: "))
    if menu == 1:
        Register_Login.register()
    elif menu == 2:
        Register_Login.login()
    elif menu == 3:
        exit()
