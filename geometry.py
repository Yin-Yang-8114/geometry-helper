exit1 = True
while exit1:
    user_choice = input(f'welcome to geometry helper \n please enter your choice: \n 1) calculator  : \n 2) Triangle area calculator:  \n 3) Square area calculator:  \n 4) Circle area calculator:  \n 5) Pythagoras triad checker : \n 6) Exit : \n ')
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
        pass
    elif user_choice == "3":
        pass
    elif user_choice == "4":
        pass
    elif user_choice == "5":
        pass
    elif user_choice == "6":
        print("goodbye")
        exit1 = False
