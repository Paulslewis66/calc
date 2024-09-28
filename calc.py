from operator import sub
from functools import reduce

print("Please Select a Mathemat Operation")
print("=======================")
print("1 - Add number ")
print("2 - Subtract numbers ")
print("3 - multipy numbers")
print("4 - Divide numbers")
print("5 - quit")

def showmenu():
    choice = "Please Choose menu options > (1, 2, 3, 4 (quit 5))"
    menu_option = ""

    while menu_option != '5':
        menu_option = input(choice)
        if menu_option == '1':
            print("You have Chosen Add Numbers")
            numbers = input("Enter numbers separated by spaces and normal plus signs: ")
            numbers_list = numbers.split()
            numbers_list = [char for char in numbers_list if char != '+']
            numbers_list = [int(num) for num in numbers_list]
            total_sum = sum(numbers_list)
            print("the ansswe is", total_sum)
            
        elif menu_option == '2':
            print("You have chosen Subtract Numbers")
            numbers = input("Enter numbers with spaces and minus signs : ")
            numbers_list = numbers.split()
            numbers_list = [char for char in numbers_list if char != '-']
            numbers_list = [int(num) for num in numbers_list]
            total_sum = reduce(sub, numbers_list)
            print("the ansswe is", total_sum)

        elif menu_option == '3':
            print("You Have Chosen Multiply Numbers")
            numbers = input("Enter numbers with spaces and times signs : ")
            numbers_list = numbers.split()
            numbers_list = [char for char in numbers_list if char != 'x']
            numbers_list = [int(num) for num in numbers_list]
            result = 1
            for i in numbers_list:
                result *= i
            print("the ansswe is", result)

        elif menu_option == '4':
            print("You Have Chosen Divide Numbers")
            numbers = input("Enter numbers with spaces and times signs : ")
            numbers_list = numbers.split()
            numbers_list = [char for char in numbers_list if char != '/']
            numbers_list = [int(num) for num in numbers_list]
            result = 1
            for i in numbers_list:
                result /= i
            print("the ansswe is", result)
showmenu()