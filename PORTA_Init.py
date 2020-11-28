import BIT_MATH
file = open("Dio_init.c","w")
string_data="void INIT_PORTA_DIR(void)\n{\n"
file.write(string_data)
file.close()
Value = 0b00000000
for i in range(8) :
    while(1) :
        print("Enter bit ",i,"Direction: ",end="")
        Input_Val = input()
        Input_Val=Input_Val.lower()
        if Input_Val == "in" :
            Value = BIT_MATH.CLR_BIT(Value,i)
            break;
        elif Input_Val == "out" :
            Value = BIT_MATH.SET_BIT(Value,i)
            break;
        else :
            print("Invalid choice, please try again")
file = open("Dio_init.c","a")
file.write("\tDDRA = ")
file.write(bin(Value))
file.write(";\n}")
file.close()