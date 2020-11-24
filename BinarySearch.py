list1=[5,3,2,1,-6,62,5,0,2,4,555,12]

def BinSearch(Cpy_list, Num):
    Flag = 0
    Cpy_list.sort()
    print(Cpy_list)
    LeftVal = 0
    RightVal = len(Cpy_list)-1
    Middle = int((RightVal-LeftVal+1)/2)
 
    while (LeftVal <= RightVal):
        print(LeftVal,Middle,RightVal)
        if ((Num == Cpy_list[Middle]) or (Num == Cpy_list[RightVal]) or (Num == Cpy_list[LeftVal])) :
            Flag = 1
            break;
        elif Num < Cpy_list[Middle] :
            RightVal = Middle - 1
            Middle = int((RightVal-LeftVal+1)/2)
        else :
            LeftVal = Middle + 1
            Middle = int((RightVal-LeftVal+1)/2) + LeftVal
    if Flag == 1:
        print("Number exists in the list")
    else :
        print("Number doesn't exist in the list")
    
print("Enter a number to check if it exists in the list")
num = int(input())
Val = BinSearch(list1,num)