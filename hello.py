# Output Hello World! to the screen
'''
This is a comment and it's long
So I'm going to use two lines for it
'''

import os
os.system("clear") # clears the terminal screen

print("Hello World!") # I learned about comments!
print(2 + 3)
print(5 - 1)
print(3 * 4)
print(10 / 5)
print(35 % 3) # prints remainder of the operation, eg. 2
print(2 ** 4) # prints 4 to the power of 2

print(f"3 + 2 = {3 + 2}")
print(f"5 - 1 = {5 - 1}")
print(f"3 * 4 = {3 * 4}")
print(f"10 / 5 = {10 / 5}")
print(f"35 % 3 = {35 % 3}")
print(f"2 ** 4 = {2 ** 4}")

print(5 > 1)

print(f"5 == 1: {5 == 1}")
print(f"5 != 1: {5 != 1}")
print(f"5 > 1: {5 > 1}")
print(f"5 >= 1: {5 >= 1}")
print(f"5 < 1: {5 < 1}")
print(f"5 <= 1: {5 <= 1}")

my_name = "Tim Mitra"
print(my_name)

number_1 = 5
number_2 = 10
print(number_1 + number_2)

fruit_1 = "apples"
fruit_2 = "oranges"
print("I Like " + fruit_1 + " and I like " + fruit_2)

fruit_1 = "apples"
print(fruit_1 * 5)

number_1 = 14
number_1 = number_1 + 27
print(number_1)

# user input

#####################
# Data Types
# String
# Integer
# Float
# Boolean
# List
# Tuple
# Dictionary
#####################

names = ["Tim", "Mitra", "John", "Doe"] # this is a list, it can be changed
print(names[0]) # prints the first item in the list, which is "Tim"
print(names) # prints all the names in the list

names_tuple = ("Tim", "Mitra", "John", "Doe") # this is a tuple, it cannot be changed
print(names_tuple[0]) # prints the first item in the tuple, which is "Tim"
print(names_tuple) # prints all the names in the tuple

fav_pizza = {
    "Tim": "Pepperoni",
    "Mitra": "Mushroom",
    "John": "Sausage",
    "Doe": "Veggie"
} # this is a dictionary, it can be changed
print("Tim's favorite pizza is " + fav_pizza["Tim"]) # prints Tim's favorite pizza, which is "Pepperoni"
print(fav_pizza) # prints all the names and their favorite pizzas in the

my_bool = True
print(my_bool) # prints True
my_bool = False
print(my_bool) # prints False   

# Strings
greetings= "My name is Tim Mitra"
print(greetings.upper()) # prints the string in uppercase
print(greetings.lower()) # prints the string in lowercase
print(greetings.title()) # prints the string in title case
print(greetings.capitalize()) # prints the string with the first letter capitalized
print(greetings.swapcase()) # prints the string with the case of each letter swapped
print(len(greetings)) # prints the length of the string, which is 20
print(greetings[13]) # prints the first character of the string, which is "M"
print(greetings[15:20]) # prints the characters from index 15 to 19, which is "Mitra"
print(greetings.split()[4]) # splits the string into a list of words, then prints the 5th word, which is "Mitra"
print(greetings.split(" ")[3:5]) # splits the string by a space, then prints the 4th and 5th words, which are "Tim" and "Mitra"

# Numbers

num = 10
num2 = 10.25
print(num) # prints 10
print(num2) # prints 10.25
print(float(num)) # converts num to a float and prints 10.0
print(int(num2)) # converts num2 to an integer and prints 10

print(5**2) # prints 5 to the power of 2, which is 25
print(10%2) # prints the remainder of 10 divided by 2, which is 0
print(10%3) # prints the remainder of 10 divided by 3, which is 1
print(10//3) # prints the quotient of 10 divided by 3, which is 3

print(4 + 1 * 3) # prints 7, because multiplication is done before addition 
print((4 + 1) * 3) # prints 15, because the parentheses change the order of operations
print(str(num)) # converts num to a string, which is "10"
print(int(str(num)) + 5) # converts str_num to an integer and adds 5, which prints 15
