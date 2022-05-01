
fruits = ["Apple" , "Pear" , "Orange"]

# TODO: Catch the exception and make sure the code runs without crashing.

def make_pie(index):
    try:
        friut = fruits[index]
    except IndexError: 
        print("Fruit pie")
    else:
        print(friut + "pie")

make_pie(4)
