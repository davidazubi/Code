# Task 1
list1 = [5, 'a', 7]
b = list1[1]

# task 2
a = [1, 2, 3, 4]
b = a + [5]
b[0] = 0

# Task 3
a = (1, 2, 3, 4)
a_list = list(a)
a_list.append(5)
a_list[0] = 0
b = tuple(a_list)

# Task 4
a = {'a':1, 'b':2}
a['c'] = 3

# Task 5
num_list = list(range(100))
scliced_list = num_list[50:70:3]

# Task 6
import re
a = 'element1,element2;element3;element4;element5,element6'
b = list(re.split(',|;', a))
b = ':'.join(b[::-1])



