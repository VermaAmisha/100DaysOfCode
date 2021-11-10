# # Reproduce the Bug

# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)     # the index starts from 0 and since there the 6 elements in the list, the last number should be 5
# print(dice_imgs[dice_num])   

from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])
