import random
import string

def make_gibberish(length=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

print(make_gibberish())       # random 6-letter word
print(make_gibberish(10))     # random 10-letter word
