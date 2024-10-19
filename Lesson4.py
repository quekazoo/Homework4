lst = [0, 1, 0, 12, 3]
position_in_list = 0
for i in range(len(lst)):
    if lst[i] != 0:
        lst[position_in_list] = lst[i]
        position_in_list += 1
for i in range(position_in_list, len(lst)):
    lst[i] = 0
print(lst)