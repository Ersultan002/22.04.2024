def mutiple(x,y):
    return(x*y)
a=mutiple(4,4)
print(a)

def mutiple(x,y):
    print(x*y)
a=mutiple(4,8)
print(a)

def mutiple(x,y):
    pass
a=mutiple(4,8)
print(a)

def mutiple(x,y):
    print(x*y)
    return (x*y)
a=mutiple(6,8)
print(a)

def mutiple(x,y=10):
    print(x*y)
    return(x*y)
a=mutiple(4)
print(a)


def add(x,y):
    return(x+y)
a=add(500,5)
if a<100:
    print(a,"100 ден кіші")
else :
    print(a,"100 ден улкен")


def check_numbers(x,y):
    if x+y>100:
        return "100 den kishi"
    else:
        return"100 den kishi"
print(check_numbers(100,40))



def find_max(list1):
    max_number = list1[0]
    for i in list1:
        if i > max_number:
            max_number = i
    return max_number

print(find_max([1,85,3,22,5]))


def find_max(list1):
    min_number = list1[0]
    for i in list1:
        if i < min_number:
            min_number = i
    return min_number

print(find_max([1,85,3,22,5]))


def find_max(list1):
    min_number = list1[0]
    a=0
    for i in range (len(list1)):
        if list1[i] > min_number:
            min_number = list1[i]
            a = i
    return a

print(find_max([1,8,3,22,5]))