#Luke Erdman July 23, 2024
#Need to determine how many trees you would encounter from moving right 3 and down 1 every line.
trees = 0
#answer variable
path = 0
f = open("input.txt.day3")
#opens map of trees
for line in f.readlines():
    if line[path] == "#":
        trees += 1
    #so since path is 0, if there is a # in the first place then trees with +1.
    path += 3
    #Then after that is run path is updated to 3
    if path >= 31:
        path = path - 31
    #since they say the lines just repeat, once path = 31 or higher it must be reset. Since it repeats ever 31 characters if you subtract 31 from it you will continue the pattern without having to create more charaters in the line.
#after the first line is run the next line is run with the new path variable and it repeats until the answer is given.

print(trees)