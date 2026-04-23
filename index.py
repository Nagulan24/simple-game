import random
# this the guessing game code
def choose_difficulty():
    print("\nChoose Difficulty:")
    print("1. Easy (1–50, 10 attempts)")
    print("2. Medium (1–100, 7 attempts)")
    print("3. Hard (1–200, 5 attempts)")
    
    while True:
        choice = input("Enter choice (1/2/3): ").strip()
        if choice == "1":
            return 50, 10
        elif choice == "2":
            return 100, 7
        elif choice == "3":
            return 200, 5
        else:
            print("Invalid choice. Try again.")

def play_game():
    max_num, attempts = choose_difficulty()
    number = random.randint(1, max_num)

    print(f"\nI have picked a number between 1 and {max_num}.")

    for attempt in range(1, attempts + 1):
        while True:
            guess_input = input(f"Attempt {attempt}/{attempts}: Enter your guess: ").strip()
            
            if not guess_input.isdigit():
                print("Enter a valid number.")
                continue
            
            guess = int(guess_input)
            break

        if guess == number:
            score = (attempts - attempt + 1) * 10
            print(f"🎉 Correct! You scored {score} points.")
            return score
        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")

    print(f"❌ You lost. The number was {number}.")
    return 0

def main():
    total_score = 0
    print("=== Welcome to Number Guessing Game ===")

    while True:
        total_score += play_game()
        print(f"\nTotal Score: {total_score}")

        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()