fruits = ["apple", "pear", "banana"]
berries = ["strawberry", "blueberry", "blackberry"]
vegetables = ["carrot", "kale", "cucumber"]

# lisää listat yhteen listaan
inventory = [fruits, berries, vegetables]

for items in inventory:
    for item in items:
        print(item)
