list1 = [i**2 for i in range(10)]
list2 = ['a','b']*5
list3 = ['c' if i%2==0 else i for i in range(10)]

list4 =[0]*30
list4 [0::3] = list1
list4 [1::3] = list2
list4 [2::3] = list3

print(list4)

