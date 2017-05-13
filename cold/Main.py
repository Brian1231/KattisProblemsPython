#f = open("coldTest.txt","r")


#Counts number of neg numbers in file
count = 0;
with open("coldTest.txt", "r") as f:
    for line in f:
        for s in line.split(' '):
            num = int(s) #cast s to int
            if num < 0 :
                count = count + 1
                print ("Count: %s" % count)
print ("Total: %s" % count)


import sys
 
for line in sys.stdin:
    ab = line.split()
    a = int(ab[0])
    b = int(ab[1])
    print(abs(a-b))