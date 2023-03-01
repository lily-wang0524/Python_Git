from sys import exit

def END():
    print("Game over, sorry.")
    exit(0)

def animal_room():
    print("\nwelcome to animal_room.")
    print("How much are you willing to pay?")
    choice1 = int(input("> "))
    if choice1 <= 10:
        print("Let's feeding animals.")
        END()
    else:
        animal = ["pig","dog","cat","duck"]
        print("open the door. There are many animals .")
        print("Which animal do you like? You can input 0-3.")
        n = int(input(">>> "))
        animal_like = animal.pop(n)
        print(f"The animal is {animal_like}")
        Garden()

def Garden():
    land = ["grass","pond","tree","flower"]
    print("\nWelcom to beautiful world!")
    for i in range(4):
        landscape = land[i]
        print(f"you can choice {i},where you can see {landscape}.")
    animal_gar =int(input("Do you see animal from animal_room. 0 or 1."))
    choice2 = int(input("which number do you choose? 0-3"))
    landscape_like = land[choice2]
    if animal_gar and landscape_like:
        print(f"you can see {landscape_like} here.")
        print("Good, you win.")
        exit(0)
    else:
        END()

def ticket():
    print("Hi, welcome to the game. ")
    print("Now,you have 50 yuan. How much are you willing to give?")
    num = int(input("> ")) 

    if num < 20:
        animal_room()
    elif num >= 20 and num <= 40:
        Garden()
    else:
        print("So good,you win.")

ticket()
        





    

    