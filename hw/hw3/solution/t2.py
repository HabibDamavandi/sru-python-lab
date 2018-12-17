n = int(input("Enter the size of your list:"))
inputList = []
for i in range(n) :
    x = int(input("List[%d]:"%i))
    inputList += [x]

for i in range(1,len(inputList)):
    for j in range(len(inputList)-i):
        if (inputList[j] > inputList[j+1]):
            inputList[j], inputList[j+1] = inputList[j+1], inputList[j]
    
print(inputList)
    
