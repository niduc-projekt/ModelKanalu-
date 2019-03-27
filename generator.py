def generate_f(countOfNumbers):
    import random, sys

    with open("DataGenerated.txt", 'w') as file:

        amount = countOfNumbers       #int(sys.argv[1])
        for i in range(0, amount):
            file.write(str(random.randint(0, 1)))

print("Witam z symulacji");