def isArmstrong(Int):
    strInt = str(Int)
    lenInt = len(strInt)
    SumInt = 0
    for EachDigit in strInt:
        SumInt += int(EachDigit) ** lenInt
    if SumInt == Int:
        return True
    else:
        return False
        

# test
print(isArmstrong(371))

def Armstrong_number(No1, No2):
    ASList = []
    for EachNo in range(No1, No2 + 1):
        if isArmstrong(EachNo):
           ASList += [EachNo]
    return ASList
    

# test
N1 = 12
N2 = 9814
print("Armstrong #'s from {:,d} to {:,d}: {}".format(N1, N2, Armstrong_number(N1, N2)))
print(Armstrong_number(N1, N2))