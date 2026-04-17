word = input("Enter a word: ")
count = int(input("Enter a number of times to print the word: "))

# for i in range(count):
#     indent = len(word) + i
#     print(f"{word:>{indent}}")

# print(len(word))

# for i in range(count):
#     print(" " * i, f"{word}")

# This second solution generates a space before the first print because it is two strings.

for i in range(count):
    print(" " * i + f"{word}")

# problem solved :)