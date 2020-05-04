# Java String builder implementation in Python 
# O(N) runtime complexity of string concatenation

import string
from string import ascii_lowercase
import random

class StringBuilder:
    def __init__(self, arraySize=1):
        self.array = [None] * arraySize
        self.freeSpaces = arraySize
        
    def append(self, newStr):
        for char in newStr:
            #print("current length: {}".format(len(self.array)))

            if(self.freeSpaces >= 1):
                #print("Constant insertion")
                self.__insertChar(char)
                print("Added:{}, NO COPY, data: {}".format(char, self.array))
            else:
                ## resizing ----- start
                newSize = len(self.array)*2
                newArray = [None] * newSize
                self.freeSpaces = newSize
                
                #print("RESIZED FROM {} TO {}".format(len(self.array), newSize))

                for index in range(len(self.array)):
                    newArray[index] = self.array[index]
                    self.freeSpaces -= 1
                    
                print("Added:{}, #_OF_COPIES:{}, Data:{}".format(char, len(self.array), self.array))

                self.array = newArray
                ## resizing ----- end

                self.__insertChar(char)
                
            
        #print("Free Spaces: {}".format(self.freeSpaces))
                    
    def __insertChar(self, char):
        insertIndex = len(self.array) - self.freeSpaces
        if(insertIndex >= 0 and insertIndex <= len(self.array)-1):
            self.array[insertIndex] = char
            self.freeSpaces -= 1
        else:
            raise Exception('Index out of bound !!')
            
    def toString(self):
        return "".join(str(v) for v in self.array if v is not None)
            
    def occupiedSpaces(self):
        return len([str(v) for v in self.array if v is not None])
            
    def spacesLeft(self):
        return self.freeSpaces
    
    def totalCapacity(self):
        return len(self.array)
    
    def randomString(self, stringLength=8):
        letters = ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))
    
sb = StringBuilder()

sb.append("Hello World !!!")

#sb.append(sb.randomString(32))
#sb.append('d')

print("\n-----------------------")
print("Total Capacity: {}".format(sb.totalCapacity()))
print("Occupied Spaces: {}".format(sb.occupiedSpaces()))
print("Spaces left: {}".format(sb.spacesLeft()))
print("-----------------------")

'''
counter = 2
while counter <= 32:
    #print(counter)
    sb.append(sb.randomString(counter))
    sb.toString()
    counter *= 2
'''
