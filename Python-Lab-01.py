#Problem 8

num1 = 6
num2 = 9

square = num1 ** 2
cube = num2 ** 3

print("Square of", num1, "=", square)
print("Cube of", num2, "=", cube)

#Problem 9
Banana = 25
Watermelon = 30
Total_fruit = Banana+Watermelon
print("Total number of fruits ", Total_fruit)

#Problem 9
principal = float(input("Enter your principal amount"))
int_rate = float(input("Enter your Interest rate"))
time = float(input("Enter the time"))
Interest = (principal*int_rate*time)/100
print("Your interest",Interest)

#Problem 10
number = 11
number_str = str(number)
print("Print integer to string", number_str)

flt = 22.5
flt_int = int(flt)
print("Print float to Integer", flt_int)

str1 = "15.5"
str_flt = float(str1)
print("Printing string to float", str_flt)

#Problem 11
animal = "bull"
typ = "domestic"
together = ((animal)+" is a "+(typ)+ "  animal")
print(together)

# Problem 12 ----List Operations
before_add = ["Orange", "Banana", "Apple", "Carrot"]
before_add.append("Blood Orange")
print("Updated list   ",before_add)


#Problem 13   List elements
fruits = ["Orange", "Banana", "Apple", "Carrot"]
print("Print the first fruit  ", fruits[0])
print("Print the second fruit  ", fruits[3])

#Problem 14 ----Dictionary
individual = {"Name": "Human", "Age": 30, "criminal record" : "No", "Location":"Chicago"}
print("Name of the person-->", individual["Name"], "And his location-->", individual["Location"])

#Problem 15 -----Adding to Dictionary
individual = {"Name": "Human", "Age": 30, "criminal record" : "No", "Location":"Chicago"}
print("Name of the person-->", individual["Name"], "And his location-->", individual["Location"])
individual["email"] = "no-one@human.com"  ###Adding to the dictionary
print("Updated dictionary:", individual)

#Problem 16 ----Basic String
text = "Welcome to the new Era!"
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))


#Problem 17 ----List Slicing
numbers = [10, 20, 30, 40, 50]
print("First three elements:", numbers[:3])
print("Last two elements:", numbers[-2:])

#Problem 18---String Formatting
kind = "Tiger"
location = "Jungle"
print("My name is {} and I am {} years old.".format(kind, location))

# Or using f-strings
print(f"This is {kind} and It lives in the {location} peacefully.")

#Problem 19 Calculating perimeter of a Circle
import math

radius = float(input("Enter the radius of the circle: "))
perimeter = 2 * math.pi * radius
print("The perimeter of the circle is:", perimeter)

#Problem 20---Boolean operation
a = 20
b = 10
c = 25

print("a > b:", a > b)   # True
print("a < c:", a < c)   # True
print("a == c:", a == c) # False
print("a != b:", a != b) # True
print("a >= 10:", a >= 10) # True
print("b <= 5:", b <= 5)  # True
