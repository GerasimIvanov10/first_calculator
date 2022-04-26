# This function adds two numbers
def add(x, y):
    return x + y

# This function substracts two numbers
def substract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num_one = int(input("Enter first number: "))
        num_two = int(input("Enter second number: "))

        if choice == '1':
            print(num_one, "+", num_two, "=", add(num_one, num_two))
        elif choice == '2':
            print(num_one, "-", num_two, "=", substract(num_one, num_two))
        elif choice == '3':
            print(num_one, "*", num_two, "=", multiply(num_one, num_two))
        elif choice == '4':
            print(num_one, "/", num_two, "=", substract(num_one, num_two))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
        else:
            print("Invalid input")
