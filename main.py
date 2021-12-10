import quantumrandom
import random

print("==============================================")
print("Quantum number generator")
print("==============================================")
print("Getting quantum data from (https://qrng.anu.edu.au)...")
print("----------------------------------------------")

data = quantumrandom.get_data()
number = data[0]

random.seed(number)

options = {
    0: "Random number",
    1: "Random number from a range"
}

print("==============================================")
print("Which type of random number would you like?")
print("----------------------------------------------")
for x in options:
  print(str(x) + ") " + options[x])
print("==============================================")

type = None
while not isinstance(type, int):
    type = input ("[" + " / ".join(str(x) for x in options.keys()) + "]: ")
    if type.isdigit() and int(type) in options.keys():
        type = int(type)
    else:
        print("Error: input must be an integer from the options listed")

if type == 0:
    output = random.random()
elif type == 1:
    start = None
    while not isinstance(start, int):
        start = input ("Whats the start of the range? ")
        if(start.isdigit()):
            start = int(start)
        else:
            print("Error: input must be an integer")
    end = None
    while not isinstance(end, int):
        end = input ("Whats the end of the range? ")
        if(end.isdigit()):
            end = int(end)
        else:
            print("Error: input must be an integer")
    output = random.randint(start, end)

print("==============================================")
print("Output: " + str(output))
