import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_person_index = random.randint(0,len(friends)-1)
random_person = friends[random_person_index]

print(random_person)