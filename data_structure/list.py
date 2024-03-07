num_list = [1, 2, 4, 6, 8, 11, 14, 19]

#one line
even = [num_even for num_even in num_list if num_even % 2 == 0]
print(even)
#RESULT: [2, 4, 6, 8, 14]



#more lines
odd = []
for num_odd in num_list:
    if num_odd % 2 == 1:
        odd.append(num_odd)
print(odd)
#RESULT: [1, 11, 19]



#num squared
squared_num = []
for num_squared in num_list:
    squared_num.append(num_squared ** 2)
print(squared_num)

#one line
squared_num_one_line = [number_squared ** 2 for number_squared in num_list]
print(squared_num_one_line)