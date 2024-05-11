def add_num(num1, num2):
    sum_val = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum_val}")
    return sum_val

def sub_num(num1, num2):
    diff = num1 - num2
    print(f"The difference of {num1} and {num2} is {diff}")
    return diff

def mul_num(num1, num2):
    mul = num1 * num2
    print(f"The multiplication of {num1} and {num2} is {mul}")
    return mul

def div_num(num1, num2):
    if num2 != 0:
        div = num1 / num2
        print(f"The division of {num1} by {num2} is {div}")
        return div
    else:
        print("Cannot divide by zero")
        return None

def main():
    while True:
        proceed = input("Continue calculation operation (Yes/No): ")
        if proceed.lower() == 'yes':
            print("**Operations to be performed**")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            choice = input("Enter a choice from 1-4: ")

            if choice == '1':
                num1 = float(input("Enter the first number to perform Addition: "))
                num2 = float(input("Enter the second number to perform Addition: "))
                add_num(num1, num2)
            elif choice == '2':
                num1 = float(input("Enter the first number to perform Subtraction: "))
                num2 = float(input("Enter the second number to perform Subtraction: "))
                sub_num(num1, num2)
            elif choice == '3':
                num1 = float(input("Enter the first number to perform Multiplication: "))
                num2 = float(input("Enter the second number to perform Multiplication: "))
                mul_num(num1, num2)
            elif choice == '4':
                num1 = float(input("Enter the first number to perform Division: "))
                num2 = float(input("Enter the second number to perform Division: "))
                div_num(num1, num2)
            else:
                print("Invalid choice. Please enter a choice between 1-4")
        else:
            print("Exiting calculation process")
            break

main()
