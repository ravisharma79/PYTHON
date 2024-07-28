import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
Symbols = "!@#$%^&*()_-><[]"

all_chars = lower_case + upper_case + numbers + Symbols
length = int (input("ENTER A LENGTH : "))

password = "".join(random.sample (all_chars, length))
print("Generated Password: " , password)
