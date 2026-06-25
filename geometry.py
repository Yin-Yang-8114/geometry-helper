exit1 = True
while exit1:
    user_choice = input(f'welcome to geometry helper \n please enter your choice: \n 1) calculator   \n 2) Triangle area calculator  \n 3) Square area calculator  \n 4) Circle area calculator  \n 5) Pythagoras triad checker  \n 6) Exit  \n right here your choosen number: ')
    if user_choice == "1":
        user_commends = input('Enter tow numbers and between them the operator: ')
        user_comments = user_commends.split()
        num1 = int(user_comments[0])
        num2 = int(user_comments[2])
        operator = user_comments[1]
        match operator:
            case '+':
                print(f'{num1} plus {num2} = {num1 + num2}')
            case '-':
                print(f'{num1} minus {num2} = {num1 - num2}')
            case '*':
                print(f'{num1} multiply {num2} = {num1 * num2}')
            case '/':
                if num2 != 0:
                    print(f'{num1} divided  {num2} = {num1 / num2}')
                else:
                    print("number cannot be divided by zero")
            case '**':
                print(f'{num1} power of  {num2} = {num1 ** num2}')
            case '%':
                print(f'{num1} modulo {num2} = {num1 % num2}')
            case _:
                print("Invalid operator")
    elif user_choice == "2":
        num_height = float(input("give me num for height "))
        num_base = float(input("give me num for base "))
        calculation = num_base * num_height / 2
        print("the triangle area is:",(calculation))
    elif user_choice == "3":
        given_square_side=float(input("please enter your choosen square side: "))
        print("the square area is",given_square_side * given_square_side)
    elif user_choice == "4":
        given_circle_radius=float(input("please enter your circle radius: "))
        print("the circle erea is", given_circle_radius * 2 * 3.141592654)

    elif user_choice == "5": 
        numbers = input("giva me three num: ")
        list_numbers = numbers.split()


        list_float = []
        for list_num in list_numbers:
            list_float.append(float(list_num))
        num0 = list_float[0]
        num1 = list_float[1]
        num2 = list_float[2]
        if num0 > num1 and num0 > num2:
            if num0 ** 2 == num1 ** 2 + num2 ** 2:
                print(num0,num1,num2, "are a pythagorean triad ")
            else:
                print("are not a pythagorean triad")    
        elif num1 > num0 and num1 > num2:
            if num1 ** 2 == num0 ** 2 + num2 ** 2:
                print(num0,num1,num2, "are a pythagorean triad ")
            else:
                print("are not a pythagorean triad")    
        elif num2 > num0 and num2 > num1:
            if num2 ** 2 == num0 ** 2 + num1 ** 2:
                print(num0,num1,num2, "are a pythagorean triad ")
            else:
                print("are not a pythagorean triad") 
    elif user_choice == "6":
        print("goodbye")
        exit1 = False


