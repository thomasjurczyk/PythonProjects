import sys, math
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
    numbers = []
    numberCounts = {}
    maxCount = 0
    median = 0
    mode = []
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
        numbers.append(xNum)
        if xNum in numberCounts:
            numberCounts[xNum] += 1
        else:
            numberCounts[xNum] = 1
    if(count == 0):
        print("There are no numbers in " + fileName)
    else:
        for x in numberCounts:
            if(numberCounts[x] > maxCount):
                maxCount = numberCounts[x]
        print(str(maxCount))
        for x in numberCounts:
            if(numberCounts[x] == maxCount):
                mode.append(x)
        numbers.sort()
        numCount=len(numbers)
        if(numCount%2==0):
            median = (numbers[int(numCount/2)-1] + numbers[int(numCount/2)])/2
        else:
            median = numbers[int(math.floor(numCount/2))]
        print("Sum: " + str(sumNum))
        print("Count: " + str(count))
        print("Average: " + str(sumNum/count))
        print("Maximum: " + str(maxNum))
        print("Minimum: " + str(minNum))
        print("Range: " + str(maxNum - minNum))
        print("Median: " + str(median))
        print("Mode: " + str(mode))
    continueLoop = input('Would you like to evaluate another file? (y/n): ')
    if continueLoop != "y":
        break

