#Luke Erdman 07/18/24
#The two numbers determine the position for the letter  in the password
#Attempt to determine the number of valid passwords in the list
valid = 0
#Variables to store the list and the number of correct passwords
f = open("input.txt.day2")
#Opens the list of passwords
for line in f.readlines():
    #So instead of the list being numbers they are a combination so they must be returned by line, which is why line is used instead.
    divide = line.find(":")
    #In order to separate the password from the policy that must be upheld a new variable "divide" is created
    rules = line[0:divide]
    #To my understanding the [] serves as an area inside of the line and 0 is the beginning character. ":" is the same as "from here to" and "divide" is the varabile which ends the rules
    password = line[divide+2:len(line)-1]
    #I thought about what exactly len(line)-1 did for a while and I believe it gives you the length of the password, which then allows password to grab every letter in the spliced part of the string each time
    dash = rules.find("-")
    space = rules.find(" ")
    #unfortunately I realized afterward that retreiving only the first character won't work since some numbers are greater than 9 so more splicing is required
    number1 = int(rules[0:dash])
    number2 = int(rules[dash+1:space])
    #these are the two numbers I'll need to compare against when I find the letter
    letter = rules[space+1]
    #letter i'll need to find
    lettercount = 0
    #need variable other than valid so I don't need to make sure I add two to its value instead of one.
    if letter == password[number1-1]:
        lettercount += 1
        #so if "letter" equals the position of number1 in password minus one since indexes start at 0, letter count increases by 1
    if letter == password[number2-1]:
        lettercount += 1
        #if letter equals the position of number 2 in password then letter count increases by 1
    if lettercount == 1:
        valid += 1
        #if they both return correct then the password is invalid so valid only increases if one of them is correct.
            

f.close
#closes the input
print(valid)
#prints the answer



            
