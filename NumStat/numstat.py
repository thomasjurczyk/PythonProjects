import sys
while True:
    print('Number Stats')
    fileName = input('File name to read from = ')
    try:
        f = open(fileName, 'r')
    except:
        e = sys.exc_info()[0]
        print("Error = " + str(e))
        continue
    count = 0
    maxNum = 0
    minNum = 0
    sumNum = 0
    for x in f:
        xNum = int(x)
        if(count == 0):
            maxNum = xNum
            minNum = xNum
        else:
            if(xNum > maxNum):
                maxNum = xNum
            if(xNum < minNum):
                minNum = xNum
        sumNum += xNum
        count += 1
    print("Sum: " + str(sumNum))
    print("Count: " + str(count))
    print("Average: " + str(sumNum/count))
    print("Maximum: " + str(maxNum))
    print("Minimum: " + str(minNum))
    print("Range: " + str(maxNum - minNum))
    continueLoop = input('Would you like to evaluate another file? (y/n): ')
    if continueLoop != "y":
        break

