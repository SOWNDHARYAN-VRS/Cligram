class Cligram:
    def __init__(self):

        self.data = None
        title="""
      _ _  
  ___| (_) __ _ _ __ __ _ _ __ ___  
 / __| | |/ _` | '__/ _` | '_ ` _ \ 
| (__| | | (_| | | | (_| | | | | | |
 \___|_|_|\__, |_|  \__,_|_| |_| |_|
          |___/
        """
        print(title)
        #getting user data from data.txt
        with open("data.txt","r") as f:
            self.data = f.readlines()
        f.close()

    def friends(self):
        print("\n1. Follow\n2. Following list\n3. Unfollow\n4.back")
        opt = int(input("Choose an option : "))
        if opt==1:
            self.follow()
        elif opt==2:
            self.following_list()
        elif opt==3:
            self.unfollow()
        elif inp==4:
            self.main_screen()
        else:
            print("Invalid option")
            self.friends()

    def main_screen(self):
        print("\nWelcome, "+self.name)
        print("1. Friends\n2. Posts\n3. Back")
        opt = int(input("Choose an option : "))
        
        if opt==1:
            self.friends()
        
        elif opt==2:
            self.posts()
        
        elif opt==3:
            self.menu()

    def login(self):
        self.name =input("Enter a name : ")
        self.pwd = input("Enter a secure password : ")

        for i in self.data:
            user, pwd = i.split("~")
            if user == self.name and pwd==self.pwd:
                self.main_screen()
                break

        print("Unable to login")
        self.menu()

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
        print("""
        ----------------------------
        | 1. Create Account         |
        | 2. Login                  |
        | 3. Exit                   |
        ---------------------------- 
         """) 
    try:    
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
   except:
        print("Enter a valid number")
        self.menu()

Cligram().menu()
