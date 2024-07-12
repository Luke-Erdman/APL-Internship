#Luke Erdman 07/12/24
#Storing empty variables
numbers = []
numbers2 = []
numbers3 = []
result = 0
product = 0

print("hello world")
f = open("input.txt")
#f is a variable of the type file pointer. "Open" opens the file and f points to the file. Allows for the f.readlines below.

#For loop is saying for "whatever" in f.readlines, f.readlines returns, once every line of the file, item.
for item in f.readlines():
    #numbers is a list. append is a function inherit to all lists. In the brackets, we're casting item to be interpreted as a number. Append means we're growing the end of the list with each item. 
    numbers.append(int(item))
numbers2 = numbers.copy()
numbers3 = numbers.copy()
#Find two numbers that sum to 2020, multiply together, print product.
#Get each number from the list.
#Take one of the lists and create a for loop. 
for entry in numbers:
    for entry2 in numbers2:
        for entry3 in numbers3:
            result = entry + entry2 + entry3
            if (result == 2020):
                product = entry * entry2 * entry3
                print("The product is " + str(product))
