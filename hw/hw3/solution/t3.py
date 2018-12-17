dic = {}

for i in range(10) :
    name = input("Name[%d]:"%i)
    number = input("Phone number[%d]:"%i)
    dic[name] = number

print(dic)

name = input("Enter a name:")
print("The phone number of %s is:" % name, dic[name])
