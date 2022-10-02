import pyfiglet
from includes import mainscreen


def create_account():
    name =input("Enter a name : ")
    pwd = input("Enter a secure password : ")
    
    with open("data.txt","r") as f:
        data = f.readlines()
    f.close()

    #checks
    for i in data:
        if name in i:
            print("Invalid username\n")
            menu()
    data.append(name+"~"+pwd)

    with open("data.txt","w") as f:
            f.writelines(data)
    f.close()

def login():
    name =input("Enter a name : ")
    pwd = input("Enter a secure password : ")
    with open("data.txt","r") as f:
        data = f.readlines()
    f.close()

    for i in data:
        user, pawd = i.split("~")
        if user == name and pwd==pawd:
            mainscreen.main_screen()
            break

def menu():
    print("1. Create Account\n2. Login\n3. Exit\n") 
    opt = int(input("Choose an option : "))

    if(opt==1):
        create_account()
    elif opt==2:
        login()
    elif opt==3:
        exit()
    else:
        print("Invalid option\n")
        menu()

print(pyfiglet.figlet_format("cligram"))
menu()
    
