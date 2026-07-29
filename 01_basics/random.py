import random

n = random.randint(1, 6)
if n == 1:
    print("大吉")
elif n == 2:
    print("中吉")
elif n == 3:
    print("小吉")
elif n == 4:
    print("末吉")
elif n == 5:
    print("凶")
else:
    print("大凶")