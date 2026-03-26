import random
import os
from datetime import datetime

# Clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Welcome screen
def display_welcome():
    print("=" * 50)
    print("🎮 NUMBER GUESSING GAME 🎮")
    print("=" * 50)
    print("Guess the number between 1 and 100")
    print("Good luck!")
    print("=" * 50)

# Get valid input
def get_valid_guess():
    while True:
        try:
            guess = int(input("👉 Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("❌ Enter number between 1 and 100")
        except ValueError:
            print("❌ Invalid input! Enter a number.")

# Difficulty levels
def choose_difficulty():
    print("\nSelect Difficulty:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == "1":
        return 10
    elif choice == "2":
        return 7
    elif choice == "3":
        return 5
    else:
        print("Invalid choice! Default = Medium")
        return 7

# Game logic
def play_game():
    clear_screen()
    display_welcome()
    
    secret_number = random.randint(1, 100)
    attempts = choose_difficulty()
    attempts_taken = 0
    guesses = []
    
    print(f"\n🎯 You have {attempts} attempts!\n")
    
    while attempts_taken < attempts:
        guess = get_valid_guess()
        attempts_taken += 1
        guesses.append(guess)
        
        if guess < secret_number:
            print(f"📉 Too LOW! ({attempts - attempts_taken} left)")
        elif guess > secret_number:
            print(f"📈 Too HIGH! ({attempts - attempts_taken} left)")
        else:
            print(f"\n🎉 You WON in {attempts_taken} attempts!")
            return attempts_taken, guesses
    
    print(f"\n💥 You LOST! Number was {secret_number}")
    return None, guesses

# Scoreboard
def display_scores(scores):
    print("\n🏆 SCOREBOARD")
    print("-" * 30)
    
    if not scores:
        print("No scores yet!")
        return
    
    for i, score in enumerate(scores[:5], 1):
        print(f"{i}. {score['attempts']} attempts | {score['date']}")

# Main menu
def main():
    scores = []
    
    while True:
        clear_screen()
        print("🎮 MAIN MENU")
        print("1. Play Game")
        print("2. View Scoreboard")
        print("3. Exit")
        
        choice = input("\nEnter choice: ")
        
        if choice == "1":
            attempts, guesses = play_game()
            
            if attempts:
                scores.append({
                    "attempts": attempts,
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M")
                })
                scores.sort(key=lambda x: x["attempts"])  # Best score first
            
            print("\n📊 Your guesses:", guesses)
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            display_scores(scores)
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            print("👋 Thanks for playing!")
            break
        
        else:
            print("❌ Invalid choice!")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()