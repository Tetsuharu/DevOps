
list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]


print('Patten 1')
print('=' * 20)
for x in list1:
    if x in list2:
        print(str(x) + " in List1 and List2")
    else:
        print(str(x) + " only in List1")


print('\n')
print('Patten 2')
print('=' * 20)
def check_list(str1, str2):
    for y in str1:
        if y in str2:
            print(str(y) + " in List1 and List2")
        else:
            print(str(y) + " only in List1")

check_list(list1, list2)
