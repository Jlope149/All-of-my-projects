import hashlib
import getpass


password_manager = {}   #dictionary ; stores password and username

def create_account():
    username = input("Enter desired username: ")
    password = getpass.getpass("Enter desired password: ")  #getpass hides the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()     #hashes the password using the sha256 algorithm
    password_manager[username] = hashed_password    #stores the username and password in dictionary
    print("Account Created Successfully")

def login():
    username = input("Enter Username: ")
    password = getpass.getpass("Enter Password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password: #checks to see if password and username are in dictionary
        print("Login Successful!")
    else:
        print("Invalid Password or Username.")

def main():
    while True:
        choice = input("Input 1 to create an account, 2 to Login, or 0 to exit: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()