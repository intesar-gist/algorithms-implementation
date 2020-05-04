# Problem # 1.2 (Check if one string is permutation of other)

def isStringPermutated_SortAndCheck(strA, strB): # N LOG(N)
    if(len(strA) != len(strB)):
        return (False, "Size not equal.")
    strA = ','.join(sorted(strA)) 
    strB = ','.join(sorted(strB)) 
    
    for i in range(len(strA)):
        if(strA[i] != strB[i]):
            return False
    return True

def isStringPermutated_AuxSpace(strA, strB):
    dictA = {}
    
    # removing 1) WHITE SPACES and consider string as 2) LOWER CASE
    strA = strA.lower().strip()
    strB = strB.lower().strip()
    
    if(len(strA) != len(strB)):
        return (False, "Size not equal.")
    
    for char in strA:
        if(dictA.get(char)!=None):
            dictA[char] += 1
        else:
            dictA[char] = 1
            
    for char in strB:
        if(dictA.get(char) != None):
            dictA[char] -= 1
            
            # No need to run the code now, just return
            # dictA[char] will only be negative if an element in string two 
            # is occuring more than the specific char in first string
            if(dictA[char] < 0):
                return False
            
    for val in dictA.values():
        if(val != 0):
            return False
            
    return True

isStringPermutated_AuxSpace("Abc", "bac")
