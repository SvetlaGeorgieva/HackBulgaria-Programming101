import sql_manager
import getpass


def main_menu():
    print("Welcome to our bank service. You are not logged in. \nPlease \
        register or login")

    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            password = \
                getpass.getpass(prompt="Enter your password: ", stream=None)

            sql_manager.register(username, password)

            print("Registration Successfull")

        elif command == 'login':
            username = input("Enter your username: ")
            password = \
                getpass.getpass(prompt="Enter your password: ", stream=None)

            logged_user = sql_manager.login(username, password)

            if logged_user:
                logged_menu(logged_user)
            else:
                print("Login failed")

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = \
                getpass.getpass(prompt="Enter your password: ", stream=None)
            sql_manager.change_pass(new_pass, logged_user)

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")

        elif command == 'logout':
            print("You have logged out!")
            break
        else:
            print("Not a valid command")


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
