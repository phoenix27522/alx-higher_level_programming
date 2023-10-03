#!/usr/bin/python3
import random
num = random.randint(-100, 100)
if num > 0:
    print(f"{num} is posetive")
elif num == 0:
    print(f"{num} is zero")
else:
    print(f"{num} is negative")
