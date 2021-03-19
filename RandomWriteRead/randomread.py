try:
    f = open("randomnum.txt", "r")
except FileNotFoundError:
    print("randomnum.txt not found")
    quit()
print("List of random numbers in randomnum.txt:")
count = 0
for x in f:
    print(x)
    count+=1
print("Random number count: " + str(count))
