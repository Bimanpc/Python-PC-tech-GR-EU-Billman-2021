import random
import string

def flipaCoin():
    return random.choice([True,False])

for i in range(0,5):
    print(flipaCoin())
