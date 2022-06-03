#import math
#Integer reading

#with open("filename.txt", "r" ) as f:
    #for x in f:
        #print(x)


#with open("filename.txt") as f:
    
    #for lines in f:
        #lines = f.readlines()
        #print(lines)

def sumfile (filename):
    with open(filename) as f:
        sum = 0
        for line in f:
            sum += int(line)
        return sum

total = sumfile('numbers.txt')
print("The overall sum is:" ,total)