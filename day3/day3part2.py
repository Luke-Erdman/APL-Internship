#Luke Erdman July 23, 2024
#Right 1 down 1
#right 3 down 1
#right 5 down 1
#right 7 down 1
#right 1 down 2
#very similar to the other part just need 4 iterations and one addition
trees1 = 0
trees2 = 0
trees3 = 0
trees4 = 0
trees5 = 0
path1 = 0
path2 = 0
path3 = 0
path4 = 0
path5 = 0
linenumber = 0
#for fifth path
answer = 0

f = open("input.txt.day3")

for line in f.readlines():
    if line[path1] == "#":
        trees1 += 1
    path1 += 1
    if path1 >= 31:
        path1 = path1 - 31

    if (linenumber % 2 == 0):
        #got this from the answer sheet, basically it divides the integer by 2 and if the remainder is 0 then it knows the line is odd and will run
        if (line[path5] == "#"):
            trees5 += 1
        path5 += 1
        if path5 >= 31:
            path5 = path5 - 31
    linenumber += 1

f.close()
f = open("input.txt.day3")

for line in f.readlines():
    if line[path2] == "#":
        trees2 += 1

    path2 += 3
    
    if path2 >= 31:
        path2 = path2 - 31

f.close()
f = open("input.txt.day3")

for line in f.readlines():
    if line[path3] == "#":
        trees3 += 1

    path3 += 5
    
    if path3 >= 31:
        path3 = path3 - 31

f.close()
f = open("input.txt.day3")

for line in f.readlines():
    if line[path4] == "#":
        trees4 += 1

    path4 += 7
    
    if path4 >= 31:
        path4 = path4 - 31

f.close()




answer = trees1*trees2*trees3*trees4*trees5
print(answer)
