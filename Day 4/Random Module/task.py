import random

#random_integer = random.randint(1,10)
#print(random_integer)

'''random_float = random.random() * 10
print(random_float)

rounded_float = round(random_float)
print(rounded_float)

random_uniform_float = random.uniform(1,10)
print(random_uniform_float)'''

print("Welcome to the Coin Flip Game!")
result = random.randint(0,1)

if result == 1:
    print("It is Heads")
else:
    print("It is Tails")



