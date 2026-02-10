print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?: "))
    if age <= 12:
        print("$5 for the ride.")
    elif age <= 18:
        print("$7 for the ride.")
    else:
        print("$12 for the ride.")
else:
    print("Sorry you have to grow taller before you can ride.")
