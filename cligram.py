import pyfiglet

class Cligram:
    def __init__(self):
        print(pyfiglet.figlet_format("cligram"))
        self.data = None

        #getting user data from data.txt
        with open("data.txt","r") as f:
            self.data = f.readlines()
        f.close()
    
    def follow(self):
        pass

    def followers_list(self):
        pass

    def following_list(self):
        pass

    def remove_following(self):
        pass

    def friends(self):
        print("1. Follow\n2. Following list\n3. Unfollow\n4.back")

    def main_screen():
        print("1. Friends\n2. Posts\n3. Back")
        opt = int(input())
        
        if opt==1:
            self.friends()
        
        elif opt==2:
            self.posts()
        
        elif opt==3:
            self.main_screen()

    def login(Self):
        self.name =input("Enter a name : ")
        self.pwd = input("Enter a secure password : ")

        for i in self.data:
            user, pwd = i.split("~")
            if user == name and pwd==pawd:
                self.main_screen()
                break

    def create_account(self):
        name =input("Enter a name : ")
        pwd = input("Enter a secure password : ")
        
        for i in self.data:
            if name in i:
                print("Invalid username\n")
                self.menu()
        self.data.append(name+"~"+pwd)

        with open("data.txt","w") as f:
                f.writelines(self.data)
        f.close()

        self.menu()

    def menu(self):
        print("1. Create Account\n2. Login\n3. Exit\n") 
        opt = int(input("Choose an option : "))

        if opt==1:
            self.create_account()
        elif opt==2:
            self.login()
        elif opt==3:
            exit()
        else:
            print("Invalid option\n")
            self.menu()

Cligram().menu()