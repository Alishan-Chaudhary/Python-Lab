fruits = ["apple","mango",'watermelon','lemon']

modified_fruits = [mod_fruit.upper() if mod_fruit.lower().startswith('a') else mod_fruit.lower() for mod_fruit in fruits]
print(modified_fruits)