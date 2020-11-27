Temp_Dict={

}
Employees={

}
while(1):
    print("|*********************************|\n| To add new employee Press 1 |\n| To print employee data Press 2 |\n| To delete employee Press 3 |\n| To Exit Press 0 |\n|*********************************|\nPlese enter your choice ", end = "")
    choice = int(input())
    if choice == 1 :
        print("Please enter Employee name: ",end = "")
        Temp_Dict["Name"] = input()
        print("Please enter Employee ID: ",end = "")
        Temp_Dict["ID"] = input()
        print("Please enter Employee Salary: ",end = "")
        Temp_Dict["Salary"] = input()
        Employees[Temp_Dict["ID"]] = Temp_Dict.copy()
    elif choice == 2 :
        print("Please enter Employee ID: ",end = "")
        choice = input() 
        if choice in Employees :
            print("Employee ID: ",end = "")
            print(Employees[choice]["ID"])
            print("Employee name: ",end = "")
            print(Employees[choice]["Name"])
            print("Employee Salary: ",end = "")
            print(Employees[choice]["Salary"])
        else :
            print("ID not found, please try again")
    elif choice == 3 :
        print("Please enter Employee ID: ",end = "")
        choice = input()
        if choice in Employees :
            Employees.pop(choice)
            print("Employee data deleted successfully")
        else :
            print("ID not found, please try again")
    elif choice == 0 :
        exit()
    else :
        print("Invalid choice, please try again")