
exit1 = True
while exit1:
    user_choice = input(f'welcome to geometry helper \n please enter your choice: \n 1) calculator  : \n 2) Triangle area calculator:  \n 3) Square area calculator:  \n 4) Circle area calculator:  \n 5) Pythagoras triad checker : \n 6) Exit : \n ')
    if user_choice == "1":
        pass
    elif user_choice == "2":
        pass
    elif user_choice == "3":
        given_square_side=float(input("please enter your choosen square side: "))
        print("the square area is",given_square_side * given_square_side)
    elif user_choice == "4":
        given_circle_radius=float(input("please enter your circle radius: "))
        print("the circle erea is", given_circle_radius * 2 * 3.141592654)

    elif user_choice == "5":
        pass
    elif user_choice == "6":
        print("goodbye")
        exit1 = False

