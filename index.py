import random
import time

high_score = 0

def choose_difficulty():
    levels = {
        "1": (50, 10),
        "2": (100, 7),
        "3": (200, 5),
        "4": (500, 8)
    }

    print("\nChoose Difficulty:")
    print("1. Easy  2. Medium  3. Hard  4. Advanced")

    while True:
        choice = input("Enter choice: ").strip()
        if choice in levels:
            return levels[choice]
        print("Invalid choice.")

def get_hint(number, guess):
    diff = abs(number - guess)
    if diff == 0:
        return "Perfect!"
    elif diff <= 5:
        return "🔥 Very Hot"
    elif diff <= 15:
        return "🌡️ Warm"
    else:
        return "❄️ Cold"

def ai_suggestion(low, high):
    return (low + high) // 2

def play_game():
    global high_score

    max_num, attempts = choose_difficulty()
    number = random.randint(1, max_num)

    lower, upper = 1, max_num
    score = 100
    hints_left = 3
    start_time = time.time()

    print(f"\nGuess the number between {lower} and {upper}")

    for attempt in range(1, attempts + 1):

        print(f"\nAttempt {attempt}/{attempts}")
        print(f"Range: {lower} - {upper}")

        user_input = input("Enter guess / 'hint' / 'ai': ").strip().lower()

        if user_input == "hint":
            if hints_left > 0:
                hints_left -= 1
                print(f"💡 Hint: Number is {'even' if number % 2 == 0 else 'odd'}")
                score -= 10
            else:
                print("No hints left!")
            continue

        if user_input == "ai":
            suggestion = ai_suggestion(lower, upper)
            print(f"🤖 AI suggests: {suggestion}")
            score -= 5
            continue

        if not user_input.isdigit():
            print("Invalid input.")
            continue

        guess = int(user_input)

        if guess == number:
            time_taken = int(time.time() - start_time)
            time_bonus = max(0, 50 - time_taken)
            score += time_bonus

            print("\n🎉 Correct!")
            print(f"⏱ Time bonus: {time_bonus}")
            print(f"🏆 Final Score: {score}")

            if score > high_score:
                high_score = score
                print("🔥 New High Score!")

            return

        elif guess < number:
            print("Too low.", get_hint(number, guess))
            lower = max(lower, guess + 1)

        else:
            print("Too high.", get_hint(number, guess))
            upper = min(upper, guess - 1)

        score -= 10  # penalty per wrong guess

    print(f"\n❌ You lost! Number was {number}")
    print(f"Score: {score}")

def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()