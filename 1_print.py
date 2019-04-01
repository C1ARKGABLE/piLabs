# import time library
import time


# Print a string to output
print("Hello there!")

# Wait 1 second
time.sleep(1)

# Define a string
string = "My name is pi."

# Print predefined string
print(string)

# Wait 500 milliseconds
time.sleep(.5)


# Save user input to a variable (Aka their name)
variable = input("What's your name? ")

# Wait 1 second
time.sleep(1)


# Print a string with a variable in the middle
print("Hello {0}, it's nice to see you.".format(variable))

# Advanced printing!
# Define a list of fruits
fruits = ["Apples", "Bananas", "Oranges", "Peaches", "Raspberries"]

# Print out the preliminary statement without a line break
print("I like ", end="")

# For each fruit in fruits, where fruit = fruits[i]
for i, fruit in enumerate(fruits):
    # Print which the fruit
    print(fruit, end="")
    # If we're not at second to last element
    if i < len(fruits) - 2:
        # Print a comma
        print(", ", end="")
    # If we're at the second to last element
    elif i == len(fruits) - 2:
        # Print "and" with an oxford comma
        print(", and ", end="")
    # Else (we're probably at the end of the list)
    else:
        # Print a period with a line break
        print(".")

        # aka 'print(".", end="\n")''
