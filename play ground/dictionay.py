fruit = {'mango':150, 'banana' : 50, 'apple': 100}
print(fruit)

mango_price = fruit.get('mango')
print(mango_price)

vegetable = {1:{'potato':50, 'type':'big'},2:{'onion':100, 'type':"medium"}}
get_price = vegetable.get(2).get('type')
print(get_price)

vegetable[3] = 'garlic'
print(vegetable)

dict_items = fruit.items()
print(dict_items)

# fruit.clear()
# print(fruit)

revome = vegetable.pop(1)
print(revome)

dict_2 = fruit.copy()
print(dict_2)

print(fruit.values())