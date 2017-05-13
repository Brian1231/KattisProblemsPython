import string
import random
import time

possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'

target = input("Enter your target text: ")
attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(target)))
attemptNext = ''

completed = False

generation = 0
index = 0
while completed == False:
    print(attemptThis)
    attemptNext = ''
    completed = True
    
    for i in range(len(target)):
        if attemptThis[i] != target[i]:
            completed = False
            attemptNext += possibleCharacters[index]
        else:
            attemptNext += target[i]
    index = (index + 1)%len(possibleCharacters)
    generation += 1
    attemptThis = attemptNext
    time.sleep(0.1)

print("Target matched! That took " + str(generation) + " generation(s)")