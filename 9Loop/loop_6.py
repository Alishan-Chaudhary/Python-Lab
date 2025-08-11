number = [1,4,5,7,8,11,12,15,18]
in_list = list(number)
new_list = list()

for i in in_list:
    if i == 5:
        continue
    if i == 15:
        break
    if i%2 == 0:
        new_list.append(i*2)
    
    elif i%2 != 0 :
        print(i*3)
