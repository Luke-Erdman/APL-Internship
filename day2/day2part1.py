#Luke Erdman 07/17/24
#The two numbers determine the range for the number the letter can appear in the password
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
    #letter ill need to find number of
    lettercount = 0
    #number of letters
    for g in password: 
        if g == letter:
            #so if this variable g, which changes every time the next character in password is used, equals letter, then lettercount should increase by 1
            lettercount += 1
    if(lettercount >= number1) and (lettercount <= number2):
            valid += 1
            #after the for loop has run for the entirety of the password, then this if statement will run and the valid variable will be corrected
#after the entire for loop is run, it will continue to the next line and repeat until the end of the input

f.close
#closes the input
print(valid)
#prints the answer



            
