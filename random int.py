import random

for i in range(5):
    print(random.randint(1,100))

print("sepration")

for i in range(5):
    random.seed(1)
    print(random.randint(1,100))
