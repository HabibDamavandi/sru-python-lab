import numpy as np

class MagicSquare:
    
    def __init__(self,n):
        self.__n = n
        self.__a = np.zeros((n,n), dtype=int)

    def setSize(self,n):
        self.__n = n
        self.__a = np.zeros((n,n), dtype=int)

    def getSize(self):
        return self.__n
        
    def getSquare(self):
        col = (self.__n - 1) // 2
        row = 0        
        k = 1
        while k <= ((self.__n)**2):
            self.__a[row,col] = k
            k += 1
            newi, newj = (row-1)%self.__n, (col+1)%self.__n
            if self.__a[newi,newj]:
                row = (row+1)%self.__n
            else:
                row, col = newi, newj
        return self.__a

# Main #------------------------------

mgs = MagicSquare(7)
print("magic square of order 7:")
print(mgs.getSquare())

mgs.setSize(11)
print("magic square of order 11:")
print(mgs.getSquare())



    

