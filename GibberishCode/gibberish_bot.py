#!/usr/bin/env python3
"""
Gibberish Bot — Simple interactive terminal bot for beginners.

Commands:
  help               Show available commands
  gibberish [n]      Generate a gibberish word of length n (default 6)
  password [n]       Generate a password of length n (default 10)
  pronounceable [n]  Generate a pronounceable fake word of length n (default 6)
  quit / exit        Exit the bot
"""

import random
import string

def make_gibberish(length=6):
    """Return a random string of lowercase letters of given length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(max(1, int(length))))

def make_password(length=10):
    """Return a random password mixing letters, digits and symbols."""
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return ''.join(random.choice(chars) for _ in range(max(4, int(length))))

def make_pronounceable(length=6):
    """
    Simple pronounceable word generator:
    alternate consonant and vowel to make it easier to say.
    """
    vowels = "aeiou"
    consonants = "".join(ch for ch in string.ascii_lowercase if ch not in vowels)
    word = []
    use_consonant = True
    for i in range(max(1, int(length))):
        if use_consonant:
            word.append(random.choice(consonants))
        else:
            word.append(random.choice(vowels))
        use_consonant = not use_consonant
    return "".join(word)

def show_help():
    print("""
Gibberish Bot - commands:
  help               Show this help message
  gibberish [n]      Generate a gibberish word (default n=6)
  password [n]       Generate a password (default n=10)
  pronounceable [n]  Generate pronounceable fake word (default n=6)
  quit / exit        Exit the bot
Examples:
  gibberish 8
  password 12
  pronounceable 7
""")

def main():
    print("👋 Welcome to Gibberish Bot (type 'help' for commands)")
    while True:
        try:
            raw = input(">> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not raw:
            continue

        parts = raw.split()
        cmd = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else None

        if cmd in ("help", "?"):
            show_help()
        elif cmd == "gibberish":
            n = arg or 6
            print(make_gibberish(n))
        elif cmd == "password":
            n = arg or 10
            print(make_password(n))
        elif cmd in ("pronounceable", "fake"):
            n = arg or 6
            print(make_pronounceable(n))
        elif cmd in ("quit", "exit"):
            print("Bye 👋")
            break
        else:
            print("Unknown command. Type 'help' to see commands.")

if __name__ == "__main__":
    main()
