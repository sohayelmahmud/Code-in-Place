import random

def generate_question():
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    return num1, num2

def check_answer(num1, num2, user_answer):
    correct_answer = num1 + num2
    if user_answer == correct_answer:
        return True
    else:
        return False

def main():
    print("Khansole Academy")
    correct_in_a_row = 0
    while correct_in_a_row < 3:
        num1, num2 = generate_question()
        print("What is", num1, "+", num2, "?")
        user_answer = int(input("Your answer: "))
        if check_answer(num1, num2, user_answer):
            correct_in_a_row += 1
            print("Correct! You've gotten", correct_in_a_row, "correct in a row.")
        else:
            correct_in_a_row = 0
            print("Incorrect.")
            print("The expected answer is", num1 + num2)

    print("Congratulations! You mastered addition.")
    
    
    # TODO: your code here
    
    
if __name__ == '__main__':
    main()