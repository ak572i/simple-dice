import random
result = []
def clerror(clean):
    try:
        clean = int(input(test))
        return clean
    except ValueError:
        print("Enter a number!")
def flip(x):
    global result
    result = []
    for _ in range(x):
        coin = random.randint(1,2)
        if coin == 1:
            coin = "heads"
        if coin == 2:
            coin = "tails"
        result.append(coin)
    return result
def dice(x,y):
    global result
    result = []
    for _ in range(x):
        roll = random.randint(1,y)
        result.append(roll)
    return result
while True:
    print("Enter 1 for dice\nEnter 2 for coin flip\nEnter q to quit")
    choice = input("Enter here: ")
    if choice == "1":
        rolls = int(input("How many dice?"))
        sides = int(input("How many sides should the dice have?: "))
        dice(rolls,sides)
        print(f"You rolled {result}")
        print(f"Your rolls add up to {sum(result)}")
    elif choice == "2":
        flips = int(input("How many coin flips?"))
        flip(flips)
        print(f"You got {result}")
    elif choice == "q":
        print("Goodbye!")
        break
    elif choice not in ["1","2","q"]:
        print("Invalid choice!")