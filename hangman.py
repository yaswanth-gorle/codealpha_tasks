"""
Hangman Game — Python
Author: Claude (Anthropic) | Version: 1.0.0
"""

import random
import os

WORD_BANK = ["python", "galaxy", "bridge", "jungle", "rocket"]

MAX_WRONG = 6

STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========="""
]


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def display_word(secret, guessed):
    return " ".join(ch if ch in guessed else "_" for ch in secret)


def get_guess(used):
    while True:
        letter = input("  Guess a letter: ").strip().lower()
        if len(letter) != 1 or not letter.isalpha():
            print("  ⚠  Enter a single letter.\n")
        elif letter in used:
            print(f"  ⚠  '{letter}' already guessed.\n")
        else:
            return letter


def show_state(wrong, word_display, correct, wrong_set):
    print(STAGES[wrong])
    print(f"  Word    : {word_display}")
    print(f"  Wrong   ({wrong}/{MAX_WRONG}): {', '.join(sorted(wrong_set)) or '—'}")
    print(f"  Correct : {', '.join(sorted(correct)) or '—'}\n")


def play():
    secret = random.choice(WORD_BANK)
    guessed, correct, wrong_set = set(), set(), set()
    wrong = 0

    clear()
    print("=" * 40)
    print("       W E L C O M E  T O  H A N G M A N")
    print("=" * 40)
    print(f"\n  Word length: {len(secret)} letters")
    print(f"  Wrong guesses allowed: {MAX_WRONG}\n")

    while wrong < MAX_WRONG:
        show_state(wrong, display_word(secret, guessed), correct, wrong_set)

        if all(ch in guessed for ch in secret):
            print(f"  🎉  You won! The word was '{secret.upper()}'\n")
            return

        letter = get_guess(guessed)
        guessed.add(letter)
        clear()

        if letter in secret:
            correct.add(letter)
            print(f"\n  ✅  '{letter}' is in the word.\n")
        else:
            wrong_set.add(letter)
            wrong += 1
            print(f"\n  ❌  '{letter}' is not in the word. {MAX_WRONG - wrong} left.\n")

    show_state(wrong, display_word(secret, guessed), correct, wrong_set)
    print(f"  💀  Game over! The word was '{secret.upper()}'\n")


def main():
    while True:
        play()
        print("-" * 40)
        if input("  Play again? (y/n): ").strip().lower() not in {"y", "yes"}:
            print("\n  Thanks for playing! Goodbye. 👋\n")
            break
        clear()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Game interrupted. Goodbye! 👋\n")
