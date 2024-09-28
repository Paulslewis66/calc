print("Please Select a Mathemat Operation")
print("=======================")
print("1 - Add number ")
print("2 - Subtract numbers ")3
print("3 - multipy numbers")
print("4 - Divide numbers")
print("5 - quit")

choice = "Please Choose menu options > (1, 2, 3, 4 (quit 5))"
menu_option = ""

while menu_option != '5':
    menu_option = input(choice)
    if menu_option == '1':
        print("You have Chosen Add Numbers")
        a = 0
        b = 0
        a = input("Please Type a number > ")
        b = input("please type a second number > ")
        sum = int(a) + int(b)
        print("Answer is", sum)
     
    elif menu_option == '2':
        print("You have chosen Subtract Numbers")
        a = 0
        b= 0
        a = input("Please Type a number > ")
        b = input("please type a second number > ")
        sum = int(a) - int(b)
        print("Answer is", sum)

    elif menu_option == '3':
        print("You Have Chosen Multiply Numbers")
        a = 0
        b = 0
        a = input("Please Type a number > ")
        b = input("please type a second number > ")
        sum = int(a) * int(b)
        print("Answer is", sum) 

    elif menu_option == '4':
        print("You Have Chosen Divide Numbers")
        a = 0
        b = 0
        a = input("Please Type a number > ")
        b = input("please type a second number > ")
        sum = int(a) / int(b)
        print("Answer is", sum)