list = ['book', 'book', 'pen', 'pen', 'pen', 'pencil', 'marker']

# 1
print(list)
list.append('pen')
print(list)

# 2
count_pencil = list.count('pencil')
print(count_pencil)

# 3
list.insert(2,'Sticky notes')
print(list)

# 4
list.remove('pencil')
print(list)

# 5
remove_2nd = list.pop(1)
print(remove_2nd)
print(list)


# 6
remove_1 = list.pop(0)
remove_2 =list.pop(0)
print("removed items =", remove_1, remove_2)
print(list)

# 7
count = len(list)
print(count)

# 8
join = ",".join(list)
print(join)

# 9
print(list[0:3])

# 10 
position_pen = list.index('pen')
print(position_pen)
print(list[2])