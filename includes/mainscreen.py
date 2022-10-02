from includes import friends

def main_screen():
    print("1. Friends\n2. Posts\n3. Back")
    opt = int(input())
    
    if opt==1:
        friends.friends()
    
    elif opt==2:
        posts()
    
    elif opt==3:
        main_screen()