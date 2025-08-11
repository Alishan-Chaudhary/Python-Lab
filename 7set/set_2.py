items = ['book', 'book', 'pen', 'pen', 'pen', 'pencil', 'marker']

unique_items = set(items)
print(unique_items)

total_unique_items = len(unique_items)
print(total_unique_items)

unique_items.add('sticky notes')
print(unique_items)

unique_items.discard('pen')
print(unique_items)

