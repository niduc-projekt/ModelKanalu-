import random, sys

with open("DataGenerated.txt", 'w') as file:

    amount = 500        #int(sys.argv[1])
    for i in range(0, amount):
        file.write(str(random.randint(0, 1)))
