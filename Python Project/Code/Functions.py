import datetime
from Classes import *
import re


# Read File and add the Information to the global dictionaries
def ReadFile(F1, F2, F3, EmployeeArray, EmployeeVacationArray, EmployeeExperienceArray):
    f = open(F1, "r")
    # Read the attributes form GAttributes.txt
    for line in f:
        VacationList = {}
        ExperienceList = {}
        line = line.strip()
        Emplo = re.split('; |, |/', line)
        Date = datetime.datetime(int(Emplo[6]), int(Emplo[5]), int(Emplo[4])).date()
        DateS = datetime.datetime(int(Emplo[17]), int(Emplo[16]), 1).date()
        # Read the administrative attributes from Administrative.txt file
        f2 = open(F2, "r")
        for line2 in f2:
            line2 = line2.strip()
            Vec = line2.split("; ")
            if Vec[0] == Emplo[0]:
                VacationList[int(Vec[1])] = int(Vec[2])
            else:
                continue
        # Read the academic attributes from Academic.txt file.
        f3 = open(F3, "r")
        for line3 in f3:
            line3 = line3.strip()
            Vec = line3.split("; ")
            Courses = re.split(" ", Vec[3])
            if Vec[0] == Emplo[0]:
                ExperienceList[Vec[2] + "-" + Vec[1]] = Courses
            else:
                continue
        # Make the objects and save in the lists
        E = EmployeeClass(int(Emplo[0]), Emplo[1], Emplo[2], Emplo[3], Date, Emplo[7], int(Emplo[8]), Emplo[9],
                          Emplo[10],
                          int(Emplo[11]),
                          int(Emplo[12]), Emplo[13], Emplo[14], Emplo[15], DateS, int(Emplo[18]), Emplo[19])
        V = VacationClass(int(Emplo[0]), Emplo[1], Emplo[2], Emplo[3], Date, Emplo[7], int(Emplo[8]), Emplo[9],
                          Emplo[10],
                          int(Emplo[11]),
                          int(Emplo[12]), Emplo[13], Emplo[14], Emplo[15], DateS, int(Emplo[18]), Emplo[19],
                          VacationList)
        Exp = ExperianceClass(int(Emplo[0]), Emplo[1], Emplo[2], Emplo[3], Date, Emplo[7], int(Emplo[8]), Emplo[9],
                              Emplo[10],
                              int(Emplo[11]),
                              int(Emplo[12]), Emplo[13], Emplo[14], Emplo[15], DateS, int(Emplo[18]), Emplo[19],
                              ExperienceList)
        # Save in dictionaries
        EmployeeArray[int(E.ID)] = str(E)
        EmployeeVacationArray[int(V.ID)] = V.__str__()
        EmployeeExperienceArray[int(E.ID)] = Exp.__str__()


# here the Function must ask to enter new record for an employee that consists of all general attributes only. and check the entered data.
def AddEmployee(EmployeeArray):
    FName = ''
    MName = ''
    LName = ''

    while True:
        try:
            ID = int(
                input("Enter employee's ID (ID's Length should be 5 Numbers long and it should be unique)\n"))

            if len(str(ID)) == 5:
                if ID not in EmployeeArray:
                    break
                else:
                    print("There is Such Employee")
                    continue
            else:
                continue
        except ValueError:
            print('Only integer inputs allowed')

    while True:
        if FName.isalpha() is False:
            FName = input("Enter employee's First Name\n")
        else:
            break

    while True:

        if MName.isalpha() is False:
            MName = input("Enter employee's Middle Name\n")
        else:
            break

    while True:
        if LName.isalpha() is False:
            LName = input("Enter employee's Last Name\n")
        else:
            break
    while True:
        try:
            year = int(input("Enter the year of Birth\n"))
            if (len(str(year)) == 4) and 1900 < year < 2023:
                break
            else:
                continue
        except ValueError:
            print('Only integer inputs allowed')

    while True:
        try:
            month = int(input("Enter the Month of Birth\n"))
            if (len(str(month)) == 2 or len(str(month)) == 1) and 0 < month < 13:
                break
            else:
                continue
        except ValueError:
            print('Only integer inputs allowed')

    while True:
        try:
            day = int(input("Enter the Day of Birth\n"))
            if (len(str(day)) == 2 or len(str(day)) == 1) and day < 32:
                break
            else:
                continue
        except ValueError:
            print('Only integer inputs allowed')

    DateOfBirth = datetime.datetime(year, month, day).date()

    while True:
        try:
            MarStatus = int(input("Enter employee's Martial Status ( 1 for married 0 for single)\n"))
            if MarStatus == 1:
                sta = "Married"
                break

            elif MarStatus == 0:
                sta = "Single"
                break

            else:
                continue

        except ValueError:
            print('Only integer inputs allowed')

    while True:
        try:
            NOC = int(input("Enter employee's Number of Children\n"))
            if NOC < 70:
                break
            else:
                continue
        except ValueError:
            print('Only integer inputs allowed')

    while True:
        try:
            Gender = int(input("Enter employee's Gender Status (1 for Male 0 for Female)\n"))
            if Gender == 1:
                gen = "Male"
                break

            elif Gender == 0:
                gen = "Female"
                break

            else:
                continue

        except ValueError:
            print('Only integer inputs allowed')

    while True:
        Email = input("Enter employee's Email\n")
        while True:
            try:
                MobileNum = (input("Enter employee's Mobile number (10 Numbers)\n"))
                if len(str(MobileNum)) == 10:
                    MobileNum = int(MobileNum)
                    break

                else:
                    continue
            except ValueError:
                print('Only integer inputs allowed')
        while True:
            try:
                Fax = (input("Enter employee's Fax (9 Numbers)\n"))
                if len(str(Fax)) == 9:
                    Fax = int(Fax)
                    break
                else:
                    continue
            except ValueError:
                print('Only integer inputs allowed')
        break

    while True:
        Type = input("Enter employee's Type(Administrative or Academic)\n")
        if Type == "Academic" or Type == "Administrative":
            break
        else:
            print("The Type should be Administrative or Academic\n")
            continue
    while True:
        try:
            Status = int(input("Enter employee's Status (2 for Full-time /1 for Part-time /0 for "
                               "left-university)\n"))
            if Status == 2:
                stat = "Full-time"
                break
            elif Status == 1:
                stat = "Part-time"
                break
            elif Status == 0:
                stat = "left-university"
                break
            else:
                continue
        except ValueError:
            print('Only integer inputs allowed')
    while True:
        Department = input("Enter employee's Department\n")
        if Department.isalpha() is False:
            continue
        else:
            break
    while True:
        try:
            yearStart = int(input("Enter the Starting year\n"))
            if (len(str(yearStart)) == 4) and 1900 < yearStart < 2023:
                break
            else:
                continue
        except ValueError:
            print('Only integer inputs allowed')

    while True:
        try:
            monthStart = int(input("Enter the Starting month\n"))
            if (len(str(monthStart)) == 2 or len(str(monthStart)) == 1) and 0 < monthStart < 13:
                break
            else:
                continue
        except ValueError:
            print('Only integer inputs allowed')
    DateOfStart = datetime.datetime(yearStart, monthStart, 1).date()

    while True:
        try:
            BasicSal = int(input("Enter employee's Salary\n"))
            break
        except ValueError:
            print('Only integer inputs allowed')
            continue
    while True:
        try:
            HealInsu = int(input("Enter employee's Health Insurance(1 for true 0 for false)\n"))
            if HealInsu == 1:
                heal = "true"
                break

            elif HealInsu == 0:
                heal = "false"
                break
            else:
                continue
        except ValueError:
            print('Only integer inputs allowed')
    E = EmployeeClass(ID, FName, MName, LName, DateOfBirth, sta, NOC, gen,
                      Email,
                      MobileNum,
                      Fax, Type, stat, Department, DateOfStart, BasicSal, heal)
    EmployeeArray[int(E.ID)] = str(E)


# here the Function must ask for employee ID and then the name of the general attribute/s and finally the new value.
def UpdateEmployeeAttributes(EmployeeArray, EmployeeVacationArray, EmployeeExperienceArray):
    while True:
        try:
            OldID = int(input("Enter Employee ID to Update\n"))
            if len(str(OldID)) == 5:
                if OldID in EmployeeArray:
                    break
                else:
                    print("There is no Such Employee")
                    continue
            else:
                continue
        except ValueError:
            print('Only integer inputs allowed')
    print(EmployeeArray.get(OldID))
    Emplo = re.split('; |, ', EmployeeArray.get(OldID))
    FullName = re.split(' ', Emplo[1])
    print("1- Update ID")
    print("2- Update Name")
    print("3- Update Date of birth")
    print("4- Update Marital status")
    print("5- Update Number of Children")
    print("6- Update Gender")
    print("7- Update Contact information")
    print("8- Update Type")
    print("9- Update Status")
    print("10- Update Department")
    print("11- Update Starting time")
    print("12- Update Basic salary")
    print("13- Update Health insurance")
    print("0- Exit and Save")
    command2 = input("What do you want to update\n")
    match command2:
        case '1':
            while True:
                try:
                    NewID = int(input("Enter New Employee ID to Update\n"))
                    if len(str(NewID)) == 5:
                        if OldID in EmployeeArray and NewID not in EmployeeArray:
                            E = EmployeeClass(NewID, FullName[0], FullName[1], FullName[2], Emplo[2], Emplo[3],
                                              int(Emplo[4]), Emplo[5],
                                              Emplo[6],
                                              int(Emplo[7]),
                                              int(Emplo[8]), Emplo[9], Emplo[10], Emplo[11], Emplo[12],
                                              int(Emplo[13]), Emplo[14])
                            EmployeeArray[int(E.ID)] = str(E)
                            EmployeeVacationArray[int(E.ID)] = EmployeeVacationArray.pop(OldID)
                            EmployeeExperienceArray[int(E.ID)] = EmployeeExperienceArray.pop(OldID)
                            del EmployeeArray[OldID]
                            break
                        else:
                            print("There is no Such Employee")
                            continue
                    else:
                        continue
                except ValueError:
                    print('Only integer inputs allowed')
        case '2':
            NewFName = ''
            NewMName = ''
            NewLName = ''
            while True:
                if NewFName.isalpha() is False:
                    NewFName = input("Enter employee's First Name\n")
                else:
                    break

            while True:

                if NewMName.isalpha() is False:
                    NewMName = input("Enter employee's Middle Name\n")
                else:
                    break

            while True:
                if NewLName.isalpha() is False:
                    NewLName = input("Enter employee's Last Name\n")
                else:
                    break
            del EmployeeArray[OldID]
            E = EmployeeClass(int(Emplo[0]), NewFName, NewMName, NewLName, Emplo[2], Emplo[3],
                              int(Emplo[4]), Emplo[5],
                              Emplo[6],
                              int(Emplo[7]),
                              int(Emplo[8]), Emplo[9], Emplo[10], Emplo[11], Emplo[12],
                              int(Emplo[13]), Emplo[14])
            EmployeeArray[int(E.ID)] = str(E)
        case '3':
            while True:
                try:
                    newyear = int(input("Enter the year of Birth\n"))
                    if (len(str(newyear)) == 4) and 1900 < newyear < 2023:
                        break
                    else:
                        continue
                except ValueError:
                    print('Only integer inputs allowed')

            while True:
                try:
                    newmonth = int(input("Enter the Month of Birth\n"))
                    if (len(str(newmonth)) == 2 or len(str(newmonth)) == 1) and 0 < newmonth < 13:
                        break
                    else:
                        continue
                except ValueError:
                    print('Only integer inputs allowed')

            while True:
                try:
                    newday = int(input("Enter the Day of Birth\n"))
                    if (len(str(newday)) == 2 or len(str(newday)) == 1) and newday < 32:
                        break
                    else:
                        continue
                except ValueError:
                    print('Only integer inputs allowed')

            newDateOfBirth = datetime.datetime(newyear, newmonth, newday).date()
            del EmployeeArray[OldID]
            E = EmployeeClass(int(Emplo[0]), FullName[0], FullName[1], FullName[2], newDateOfBirth, Emplo[3],
                              int(Emplo[4]), Emplo[5],
                              Emplo[6],
                              int(Emplo[7]),
                              int(Emplo[8]), Emplo[9], Emplo[10], Emplo[11], Emplo[12],
                              int(Emplo[13]), Emplo[14])
            EmployeeArray[int(E.ID)] = str(E)
        case '4':
            while True:
                try:
                    newMarStatus = int(input("Enter employee's Martial Status ( 1 for married 0 for single)\n"))
                    if newMarStatus == 1:
                        newsta = "Married"
                        break

                    elif newMarStatus == 0:
                        newsta = "Single"
                        break

                    else:
                        continue

                except ValueError:
                    print('Only integer inputs allowed')
            del EmployeeArray[OldID]
            E = EmployeeClass(int(Emplo[0]), FullName[0], FullName[1], FullName[2], Emplo[2], newsta,
                              int(Emplo[4]), Emplo[5],
                              Emplo[6],
                              int(Emplo[7]),
                              int(Emplo[8]), Emplo[9], Emplo[10], Emplo[11], Emplo[12],
                              int(Emplo[13]), Emplo[14])
            EmployeeArray[int(E.ID)] = str(E)
        case '5':
            while True:
                try:
                    newNOC = int(input("Enter employee's Number of Children\n"))
                    if newNOC < 70:
                        break
                    else:
                        continue
                except ValueError:
                    print('Only integer inputs allowed')
            del EmployeeArray[OldID]
            E = EmployeeClass(int(Emplo[0]), FullName[0], FullName[1], FullName[2], Emplo[2], Emplo[3],
                              newNOC, Emplo[5],
                              Emplo[6],
                              int(Emplo[7]),
                              int(Emplo[8]), Emplo[9], Emplo[10], Emplo[11], Emplo[12],
                              int(Emplo[13]), Emplo[14])
            EmployeeArray[int(E.ID)] = str(E)
        case '6':
            while True:
                try:
                    newGender = int(input("Enter employee's Gender Status (1 for Male 0 for Female)\n"))
                    if newGender == 1:
                        newgen = "Male"
                        break

                    elif newGender == 0:
                        newgen = "Female"
                        break

                    else:
                        continue
                except ValueError:
                    print('Only integer inputs allowed')
            del EmployeeArray[OldID]
            E = EmployeeClass(int(Emplo[0]), FullName[0], FullName[1], FullName[2], Emplo[2], Emplo[3],
                              int(Emplo[4]), newgen,
                              Emplo[6],
                              int(Emplo[7]),
                              int(Emplo[8]), Emplo[9], Emplo[10], Emplo[11], Emplo[12],
                              int(Emplo[13]), Emplo[14])
            EmployeeArray[int(E.ID)] = str(E)
        case '7':
            while True:
                newEmail = input("Enter employee's Email\n")
                while True:
                    try:
                        newMobileNum = (input("Enter employee's Mobile number (10 Numbers)\n"))
                        if len(str(newMobileNum)) == 10:
                            newMobileNum = int(newMobileNum)
                            break
                        else:
                            continue
                    except ValueError:
                        print('Only integer inputs allowed')
                while True:
                    try:
                        newFax = (input("Enter employee's Fax (9 Numbers)\n"))
                        if len(str(newFax)) == 9:
                            newFax = int(newFax)
                            break
                        else:
                            continue
                    except ValueError:
                        print('Only integer inputs allowed')
                del EmployeeArray[OldID]
                E = EmployeeClass(int(Emplo[0]), FullName[0], FullName[1], FullName[2], Emplo[2], Emplo[3],
                                  int(Emplo[4]), Emplo[5],
                                  newEmail,
                                  newMobileNum,
                                  newFax, Emplo[9], Emplo[10], Emplo[11], Emplo[12],
                                  int(Emplo[13]), Emplo[14])
                EmployeeArray[int(E.ID)] = str(E)
        case '8':
            while True:
                newType = input("Enter employee's Type(Administrative or Academic)\n")
                if newType == "Academic" or newType == "Administrative":
                    break
                else:
                    print("The Type should be Administrative or Academic\n")
                    continue
            del EmployeeArray[OldID]
            E = EmployeeClass(int(Emplo[0]), FullName[0], FullName[1], FullName[2], Emplo[2], Emplo[3],
                              int(Emplo[4]), Emplo[5],
                              Emplo[6],
                              int(Emplo[7]),
                              int(Emplo[8]), newType, Emplo[10], Emplo[11], Emplo[12],
                              int(Emplo[13]), Emplo[14])
            EmployeeArray[int(E.ID)] = str(E)
        case '9':
            while True:
                try:
                    newStatus = int(input("Enter employee's Status (2 for Full-time /1 for Part-time /0 for "
                                          "left-university)\n"))
                    if newStatus == 2:
                        newstat = "Full-time"
                        break
                    elif newStatus == 1:
                        newstat = "Part-time"
                        break
                    elif newStatus == 0:
                        newstat = "left-university"
                        break
                    else:
                        continue
                except ValueError:
                    print('Only integer inputs allowed')
                del EmployeeArray[OldID]
                E = EmployeeClass(int(Emplo[0]), FullName[0], FullName[1], FullName[2], Emplo[2], Emplo[3],
                                  int(Emplo[4]), Emplo[5],
                                  Emplo[6],
                                  int(Emplo[7]),
                                  int(Emplo[8]), Emplo[9], newstat, Emplo[11], Emplo[12],
                                  int(Emplo[13]), Emplo[14])
                EmployeeArray[int(E.ID)] = str(E)
        case '10':
            while True:
                newDepartment = input("Enter employee's Department\n")
                if newDepartment.isalpha() is False:
                    continue
                else:
                    break
            del EmployeeArray[OldID]
            E = EmployeeClass(int(Emplo[0]), FullName[0], FullName[1], FullName[2], Emplo[2], Emplo[3],
                              int(Emplo[4]), Emplo[5],
                              Emplo[6],
                              int(Emplo[7]),
                              int(Emplo[8]), Emplo[9], Emplo[10], newDepartment, Emplo[12],
                              int(Emplo[13]), Emplo[14])
            EmployeeArray[int(E.ID)] = str(E)
        case '11':
            while True:
                try:
                    newyearStart = int(input("Enter the Starting year\n"))
                    if (len(str(newyearStart)) == 4) and 1900 < newyearStart < 2023:
                        break
                    else:
                        continue
                except ValueError:
                    print('Only integer inputs allowed')
            while True:
                try:
                    newmonthStart = int(input("Enter the Starting month\n"))
                    if (len(str(newmonthStart)) == 2 or len(
                            str(newmonthStart)) == 1) and 0 < newmonthStart < 13:
                        break
                    else:
                        continue
                except ValueError:
                    print('Only integer inputs allowed')
            newDateOfStart = datetime.datetime(newyearStart, newmonthStart, 1).date()
            del EmployeeArray[OldID]
            E = EmployeeClass(int(Emplo[0]), FullName[0], FullName[1], FullName[2], Emplo[2], Emplo[3],
                              int(Emplo[4]), Emplo[5],
                              Emplo[6],
                              int(Emplo[7]),
                              int(Emplo[8]), Emplo[9], Emplo[10], Emplo[11], newDateOfStart,
                              int(Emplo[13]), Emplo[14])
            EmployeeArray[int(E.ID)] = str(E)
        case '12':
            while True:
                try:
                    newBasicSal = int(input("Enter employee's Salary\n"))
                    break
                except ValueError:
                    print('Only integer inputs allowed')
                    continue
            del EmployeeArray[OldID]
            E = EmployeeClass(int(Emplo[0]), FullName[0], FullName[1], FullName[2], Emplo[2], Emplo[3],
                              int(Emplo[4]), Emplo[5],
                              Emplo[6],
                              int(Emplo[7]),
                              int(Emplo[8]), Emplo[9], Emplo[10], Emplo[11], Emplo[12],
                              newBasicSal, Emplo[14])
            EmployeeArray[int(E.ID)] = str(E)
        case '13':
            while True:
                try:
                    newHealInsu = int(input("Enter employee's Health Insurance(1 for true 0 for false)\n"))
                    if newHealInsu == 1:
                        newheal = "true"
                        break

                    elif newHealInsu == 0:
                        newheal = "false"
                        break
                    else:
                        continue
                except ValueError:
                    print('Only integer inputs allowed')
            del EmployeeArray[OldID]
            E = EmployeeClass(int(Emplo[0]), FullName[0], FullName[1], FullName[2], Emplo[2], Emplo[3],
                              int(Emplo[4]), Emplo[5],
                              Emplo[6],
                              int(Emplo[7]),
                              int(Emplo[8]), Emplo[9], Emplo[10], Emplo[11], Emplo[12],
                              int(Emplo[13]), newheal)
            EmployeeArray[int(E.ID)] = str(E)
        case '0':
            return
        case _:
            print("Invalid command\n")


'''the function display the following information:
• Number of academic employees,
• Number of administrative employees,
• Percent of Full-time employees,
• Number of Male employees,
• Number of Female employees,'''


def EmployeeStatistics(EmployeeArray):
    NumberOfAcademic = 0
    NumberOfAdministrative = 0
    NumberOfFull = 0
    NumberOfMale = 0
    NumberOfFemale = 0
    for employee in EmployeeArray.values():
        Emplo = re.split('; |, ', employee)
        if Emplo[9] == "Administrative":
            NumberOfAdministrative += 1
        if Emplo[9] == "Academic":
            NumberOfAcademic += 1
        if Emplo[10] == "Full-time":
            NumberOfFull += 1
        if Emplo[5] == "Male":
            NumberOfMale += 1
        if Emplo[5] == "Female":
            NumberOfFemale += 1
    print("Number of academic employees: " + str(NumberOfAcademic))
    print("Number of administrative employees: " + str(NumberOfAdministrative))
    print("Percent of Full-time employees: " + str(NumberOfFull / EmployeeArray.__len__()))
    print("Number of Male employees: " + str(NumberOfMale))
    print("Number of Female employees: " + str(NumberOfFemale))


''' the function
a. Ask for the employee ID and verify that the type of employee is administrative and the 
status not left-university. Otherwise return an error message and return to main menu.
b. For administrative employees, the program then asks for the data of the vacation 
attribute including the year and number of vacation days. If the year is already in the 
employee Vacation attribute, the project should update the number of days. Otherwise, 
it will add a new {key: value} to the Vacation attribute'''


def AddUpdateAdministrative(EmployeeArray, EmployeeVacationArray):
    while True:
        try:
            ID = int(input("Enter Employee ID\n"))
            if len(str(ID)) == 5:
                if ID in EmployeeArray:
                    break
                else:
                    print("There is no Such Employee")
                    continue
            else:
                continue
        except ValueError:
            print('Only integer inputs allowed')
    print(EmployeeArray.get(ID))
    Emplo = re.split('; |, ', EmployeeArray.get(ID))
    FullName = re.split(' ', Emplo[1])
    if Emplo[9] == "Administrative" and Emplo[10] != "left-university":
        temp = EmployeeVacationArray.get(ID)
        print("1- Add")
        print("2- Update")
        print("3- Exit")
        command3 = input("Enter command number\n")
        match command3:
            case '1':
                try:
                    print("List Of Vacations: " + str(temp))
                    year = int(input("Enter the Year of new vacation\n"))
                    if year in temp:
                        print(
                            "There such Vacation year if you want to add more days to this year go to Update\n")
                    else:
                        try:
                            days = int(input("Enter numbers of days\n"))
                            temp[year] = days
                            del EmployeeVacationArray[ID]
                            V = VacationClass(int(Emplo[0]), FullName[0], FullName[1], FullName[2], Emplo[2],
                                              Emplo[3],
                                              int(Emplo[4]), Emplo[5],
                                              Emplo[6],
                                              int(Emplo[7]),
                                              int(Emplo[8]), Emplo[9], Emplo[10], Emplo[11], Emplo[12],
                                              int(Emplo[13]), Emplo[14], temp)
                            EmployeeVacationArray[ID] = V.__str__()
                        except ValueError:
                            print('Only integer inputs allowed')
                            return
                except ValueError:
                    print('Only integer inputs allowed')
                    return
            case '2':
                try:
                    temp = EmployeeVacationArray.get(ID)
                    print("List Of Vacations: " + str(temp))
                    year = int(input("Enter the Year of vacation\n"))
                    if year not in temp:
                        print("There is no such Vacation year\n")
                    else:
                        try:
                            days = int(input("Enter numbers of days\n"))
                            temp[year] = days
                            del EmployeeVacationArray[ID]
                            V = VacationClass(int(Emplo[0]), FullName[0], FullName[1], FullName[2], Emplo[2],
                                              Emplo[3],
                                              int(Emplo[4]), Emplo[5],
                                              Emplo[6],
                                              int(Emplo[7]),
                                              int(Emplo[8]), Emplo[9], Emplo[10], Emplo[11], Emplo[12],
                                              int(Emplo[13]), Emplo[14], temp)
                            EmployeeVacationArray[ID] = V.__str__()
                        except ValueError:
                            print('Only integer inputs allowed')
                            return
                except ValueError:
                    print('Only integer inputs allowed')
                    return
            case '0':
                return
            case _:
                print("Invalid command")
                return
    else:
        return


'''the function display the following information:
• Average academic employees’ salary
• Average administrative employees’ salary 
• The names (full name) of the employees who have salaries greater than a user 
defined number. Here the program must ask user to enter this number. Note that 
the final salary is computed as:
Final salary = basic salary + 20 if the marital status is married + 15*number of 
Childs – 12 * (1 + (1 + number of Childs) if marital status is marid and joint the 
health insurance)'''


def SalaryStatistics(EmployeeArray):
    try:
        NumberOfAcademic = 0
        NumberOfAdministrative = 0
        TotalAdministrativeSalary = 0
        TotalAcademicSalary = 0
        Salary = int(input("Enter Salary limit\n"))
        for employee in EmployeeArray.values():
            Emplo = re.split('; |, ', employee)
            if Emplo[9] == "Administrative":
                NumberOfAdministrative += 1
                TotalAdministrativeSalary += int(Emplo[13])
            if Emplo[9] == "Academic":
                NumberOfAcademic += 1
                TotalAcademicSalary += int(Emplo[13])
            FinalSalary = int(Emplo[13])
            if Emplo[3] == "Maried":
                FinalSalary += 20
                if Emplo[14] == "true":
                    FinalSalary = FinalSalary - 12 * (1 + (1 + int(Emplo[4])))
            elif Emplo[3] == "Single":
                FinalSalary = FinalSalary - 12
            FinalSalary += 15 * int(Emplo[4])
            if Salary < FinalSalary:
                print("The Salary Limit= " + str(Salary))
                print(Emplo[1] + ": Final Salary= " + str(FinalSalary))
        print("The average salary of administrative employees: " + str(TotalAdministrativeSalary / NumberOfAdministrative))
        print("The average salary academic employees: " + str(TotalAcademicSalary / NumberOfAdministrative))
    except ValueError:
        print("Only integer inputs allowed")
        return


'''display the names (full name) of the employees whom have less 
than n remain years of service. You can compute this information using the staring time field 
given that maximum service years is 35 and from the date of birth filed given that 
retirement age is 65.'''


def RetirementInformation(EmployeeArray):
    try:
        Retirement = int(input("Enter years of service.\n"))
        for employee in EmployeeArray.values():
            Emplo = re.split('; |, ', employee)
            Birth = datetime.datetime.strptime(Emplo[2], '%Y-%m-%d')
            Starting = datetime.datetime.strptime(Emplo[12], '%Y-%m-%d')
            age = datetime.datetime.today().year - Birth.year - (
                    (datetime.datetime.today().month, datetime.datetime.today().day) < (Birth.month, Birth.day))
            service = datetime.datetime.today().year - Starting.year - (
                    (datetime.datetime.today().month, datetime.datetime.today().day) < (
                Starting.month, Starting.day))
            RetirementAge = Retirement + age
            RetirementService = Retirement + service
            if RetirementAge >= 65 or RetirementService >= 35:
                print("Date of birth: " + str(Birth) + ", Age: " + str(age))
                print("Starting Date: " + str(Starting) + ", Years of service: " + str(service))
                print(Emplo[1])
    except ValueError:
        print("Only integer inputs allowed")
        return


'''the function display for each administrative 
employee the following information:
• Number of vacation days the employee took since the employee started working at 
Birzeit university,
• The average number of vacation days per year for the employee. This is computed 
as the total number of vacation days divided by the number years the employee 
worked at Birzeit university'''


def AdministrativeStatistics(EmployeeVacationArray, EmployeeArray):
    TotalVec = {}
    TotalVec2 = {}
    for vec in EmployeeVacationArray:
        temp = EmployeeVacationArray.get(vec)
        for temp2 in temp.values():
            if vec in TotalVec:
                TotalVec[vec] += temp2
            else:
                TotalVec[vec] = temp2
        for days in TotalVec.values():
            if temp.__len__() != 0:
                TotalVec2[vec] = days / temp.__len__()
            else:
                continue
    print("Number of vacation For Each Employee")
    for i in TotalVec:
        Emplo = re.split('; |, ', EmployeeArray.get(i))
        print(str(i) + ": " + Emplo[1] + "= " + str(TotalVec[i]))
    print("\nThe average number of vacation days per year for the employee")
    for i in TotalVec2:
        print(str(i) + ": " + Emplo[1] + "= " + str(TotalVec2[i]))


'''the function display for each course the following information:
• Number of times the course is offered,
• Number of academic employees who taught this course.
'''


def CoursesStatistics(EmployeeArray, EmployeeExperienceArray):
    NumOfCourses = {}
    NumOfAcademic = {}
    RealNum = []
    Test = {}
    for temp in EmployeeExperienceArray.values():
        for course in temp.values():
            for c in course:
                if c in NumOfCourses:
                    NumOfCourses[c] = NumOfCourses[c] + 1
                else:
                    NumOfCourses[c] = 1
    for temp2 in EmployeeExperienceArray:
        Emplo = re.split('; |, ', EmployeeArray.get(temp2))
        Stat = Emplo[9]
        temp3 = EmployeeExperienceArray.get(temp2)
        for temp4 in temp3.values():
            for i in temp4:
                if Stat == "Academic":
                    if temp2 in NumOfAcademic:
                        NumOfAcademic[temp2] += i
                        if i not in RealNum:
                            RealNum.append(i)
                    else:
                        NumOfAcademic[temp2] = i
    for j in RealNum:
        for i in NumOfAcademic:
            Emplo = re.split('; |, ', EmployeeArray.get(i))
            if Emplo[9] == "Academic":
                if j in NumOfAcademic.get(i):
                    if j in Test:
                        Test[j] += 1
                    else:
                        Test[j] = 1

    print("Number of times the course is offered.")
    for i in NumOfCourses:
        print(str(i) + "= " + str(NumOfCourses[i]))
    print("\nNumber of academic employees who taught this course:")
    for i in Test:
        print(str(i) + "= " + str(Test[i]))


''' the function display for each academic employee the 
following information:
• Number of courses the employee taught since the employee started working at 
Birzeit university,
• The average number of courses the employee taught per semester. This is 
computed as the number of courses the employee taught at Birzeit university 
divided by the number of semesters the employee taught at Birzeit university. '''


def AcademicStatistics(EmployeeArray, EmployeeExperienceArray):
    Courses = {}
    Semesters = {}
    Avg = {}
    for temp in EmployeeExperienceArray:
        NumOfSem = EmployeeExperienceArray.get(temp).__len__()
        NumOfCourse = 0
        temp2 = EmployeeExperienceArray.get(temp)

        for course in temp2.values():
            NumOfCourse += course.__len__()
        if temp in Courses:
            continue
        else:
            Courses[temp] = NumOfCourse
        if temp in Semesters:
            continue
        else:
            Semesters[temp] = NumOfSem
    for temp in EmployeeExperienceArray:
        n1 = Courses.get(temp)
        n2 = Semesters.get(temp)
        if n1 == 0 or n2 == 0:
            continue
        else:
            Avg[temp] = n1 / n2
    print("Number of courses the employee taught.")
    for i in Courses:
        Emplo = re.split('; |, ', EmployeeArray.get(i))
        print(str(i) + ": " + Emplo[1] + "= " + str(Courses[i]))
    print("\nThe average number of courses the employee taught per semester.")
    for i in Avg:
        Emplo = re.split('; |, ', EmployeeArray.get(i))
        print(str(i) + ": " + Emplo[1] + "= " + str(Avg[i]))


'''the function Ask for the employee ID and verify that the type of employee is academic and the status 
not left-university. Otherwise return an error message and return to main menu.

For academic employees, the program then asks for the data of the Experience attribute 
including the year, semester, and courses. If the year and semester are already in the 
employee Experience attribute, the project should update the list of taught courses in 
that semester. Otherwise, it will add a new {key: value} to the Experience attribute.'''


def AddUpdateAcademic(EmployeeArray, EmployeeExperienceArray):
    while True:
        try:
            ID = int(input("Enter Employee ID\n"))
            if len(str(ID)) == 5:
                if ID in EmployeeArray:
                    break
                else:
                    print("There is no Such Employee")
                    continue
            else:
                continue
        except ValueError:
            print('Only integer inputs allowed')
    print(EmployeeArray.get(ID))
    Emplo = re.split('; |, ', EmployeeArray.get(ID))
    if Emplo[9] == "Academic" and Emplo[10] != "left-university":
        temp = EmployeeExperienceArray.get(ID)
        for i in temp.items():
            print(i)
        print(temp)
        print("1- Add")
        print("2- Update")
        print("3- Exit")
        command3 = input("Enter command number\n")
        match command3:
            case '1':
                while True:
                    try:
                        year = int(input("Enter the year\n"))
                        if (len(str(year)) == 4) and 2000 < year < 2030:
                            break
                        else:
                            continue
                    except ValueError:
                        print('Only integer inputs allowed')
                while True:
                    try:
                        semester = int(input("Enter New semester\n"))
                        if semester == 1 or semester == 2 or semester == 3:
                            break
                        else:
                            print("The Semester Number should be only 1/2/3")
                            continue
                    except ValueError:
                        print('Only integer inputs allowed')
                year_semester = str(year) + "-" + str(semester)
                print(year_semester)
                if year_semester in temp:
                    print("There such semester if you want to update it go to update\n")
                    return
                else:
                    Courses = []
                    dec = {}
                    while True:
                        course = input("Enter Course\n")
                        Courses.append(course)
                        e = input("Do you want to enter another course?(y/n)\n")
                        if e == 'y':
                            continue
                        elif e == 'n':
                            temp[year_semester] = Courses
                            EmployeeExperienceArray[ID] = temp
                            break
                        else:
                            print("Invalid, The input should y or n")
                            continue
            case '2':
                while True:
                    try:
                        year = int(input("Enter the year\n"))
                        if (len(str(year)) == 4) and 2000 < year < 2030:
                            break
                        else:
                            continue
                    except ValueError:
                        print('Only integer inputs allowed')
                while True:
                    try:
                        semester = int(input("Enter semester\n"))
                        if semester == 1 or semester == 2 or semester == 3:
                            break
                        else:
                            print("The Semester Number should be only 1/2/3")
                            continue
                    except ValueError:
                        print('Only integer inputs allowed')
                year_semester = str(year) + "-" + str(semester)
                print(year_semester)
                if year_semester in temp:
                    i = temp.get(year_semester)
                    c = input("Enter the course you want to change\n")
                    if c in i:
                        c2 = input("Enter the new course name\n")
                        i.remove(c)
                        i.append(c2)
                    else:
                        print("There is no such course")
                else:
                    print("There is no such semester\n")
            case _:
                print("Invalid input\n")
    else:
        print("The Employee is Administrative or left the university\n")
