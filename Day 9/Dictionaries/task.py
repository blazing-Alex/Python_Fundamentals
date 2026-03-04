programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
}

print(programming_dictionary["Function"])

programming_dictionary["Ultraman"] = "A show that I used to watch when I was young."
print(programming_dictionary["Ultraman"])

# Empty a dictionary

# programming_dictionary = {}
# print(programming_dictionary)

# Loop through a dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])