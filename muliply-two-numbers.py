"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""

def main():
    print("This program multiplies two numbers.")
    num_1 = int(input("Enter first number:"))
    num_2 = int(input("Enter second number:"))
    result = num_1 * num_2
    print(str(result))
    
    # your code here


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()