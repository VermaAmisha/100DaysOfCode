import random

# Here 1 means Heads and 2 means Tails

toss_result = random.randint(0,1)
# Only Heads or Tails is to be printed not the number
if toss_result == 1:
    print("Heads")
else:
    print("Tails")
