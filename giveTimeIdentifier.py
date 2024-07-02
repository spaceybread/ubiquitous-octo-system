import random
from datetime import datetime

timestamp = int(datetime.now().timestamp())
print(timestamp)

random.seed(timestamp)

poss = []

for i in range(2**16):
    poss.append(random.random())
    
# this has to be changed to noise from somewhere else
second_seed = int(datetime.now().timestamp())

random.seed(second_seed)
idx = random.randint(0, 2**16 - 1)

print(poss[idx], idx)
