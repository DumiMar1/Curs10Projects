temps = [221, 234, 340, 230]

new_temps = [temp/10 for temp in temps]

print(new_temps)

temps2 = [221, 234, 340, -9999, 230]

new_temps2 = [temp / 10 for temp in temps if temp!= -9999]
print(new_temps2)




new_list3 =[99, 'no data', 95, 94, 'no data']

no_string_list = [x for x in new_list3 if type(x) != str]

print(no_string_list)

list_4 = [-5, 3, -1, 101]

new_list4 = [x for x in list_4 if x >= 0]
print(new_list4)

list_5 = [99, 'no data', 95, 94, 'no data']

new_list5 = [x if type(x) != str else 0 for x in list_5]

print(new_list5)

new_list6 = ['1.2', '2.6', '3.3']
list_sum = sum([float(x) for x in new_list6])

print(list_sum)





