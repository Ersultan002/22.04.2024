my_list = [10,72,54,25,90,40]
max = my_list[0]
index = 0
for i in range(1,len(my_list)):
  if my_list[i] > max:
    max = my_list[i]
    index = i
 
print(f'Max index is : {index}')


def find_max(list1):
    min_number = list1[0]
    a=0
    for i in range (len(list1)):
        if list1[i] > min_number:
            min_number = list1[i]
            a = i
    return a

print(find_max([1,8,3,22,5]))