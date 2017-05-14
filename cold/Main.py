
#Counts number of neg numbers in file

cases = int(input())
numbers = input().split(" ")
count = 0
for i in numbers:
    if (int(i) < 0):
        count += 1
        
print(count)