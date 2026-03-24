print("I can tell you if an integer is odd or even.")
x = int(input("Enter an integer: "))

if x % 2 == 0:
    print(f"{x} is even.")

if x % 2 != 0:
    print(f"{x} is odd.")