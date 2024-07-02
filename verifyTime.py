import random

t = int(input())
val = float(input())

random.seed(t)

idx = 0
while True:
    a = random.random()
    if a == val:
        print(a, idx)
        break
    idx += 1
