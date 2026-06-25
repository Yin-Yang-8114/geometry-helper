# pythagoras 
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

# if max_num ** 2 == 
