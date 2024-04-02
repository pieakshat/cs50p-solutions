import random

def main():
    input_level = get_level()
    score = generate_problems(input_level)
    print(f"Your score: {score}/10")

def get_level():
    while True:
        try:
            level = int(input("Enter the level (1, 2, or 3): "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid level. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a valid level (1, 2, or 3).")

def generate_problems(level):
    score = 0
    for i in range(10):
        a = random.randint(10 ** (level - 1), (10 ** level) - 1)
        b = random.randint(10 ** (level - 1), (10 ** level) - 1)
        correct_answer = a + b
        tries = 0

        while tries < 3:
            user_answer = input(f"{a} + {b} = ")
            try:
                user_answer = int(user_answer)
                if user_answer == correct_answer:
                    print("Correct!")
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1

        if tries == 3:
            print(f"Correct answer: {correct_answer}")

    return score

if __name__ == "__main__":
    main()
