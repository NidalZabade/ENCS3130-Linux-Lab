import Functions
import os
import re
from Classes import *
import datetime

# Global Dictionary
EmployeeArray = {}
EmployeeVacationArray = {}
EmployeeExperienceArray = {}

# Read files and raise an error if the files didn’t exist.
File1 = input("Enter Attributes File\n")
FileExists1 = os.path.exists(File1)

if not FileExists1:
    print("There no such file\n")
    exit(0)

File2 = input("Enter Administrative File\n")
FileExists2 = os.path.exists(File2)

if not FileExists2:
    print("There no such file\n")
    exit(0)

File3 = input("Enter Academic File\n")
FileExists3 = os.path.exists(File3)

if not FileExists3:
    print("There no such file\n")
    exit(0)

if File1 == "GAttributes.txt" and File2 == "Administrative.txt" and File3 == "Academic.txt":
    Functions.ReadFile(File1, File2, File3, EmployeeArray, EmployeeVacationArray, EmployeeExperienceArray)

else:
    print("The files name should be GAttributes.txt then Administrative.txt then Academic.txt\n")
    exit(0)

# The Main Menu
while True:

    # The commands
    print("1- Add a new employee record")
    print("2- Update general attributes")
    print("3- Add/update administrative employee attribute")
    print("4- Add/update academic employee attribute")
    print("5- Employee’s statistics")
    print("6- Salary statistics")
    print("7- Retirement information")
    print("8- Courses statistics")
    print("9- Administrative employees’ statistics")
    print("10- Academic employees’ statistics")
    print("11- Print All Lists")
    print("0- Exit")
    command = input("Enter Command:\n")
    match command:
        case '1':
            Functions.AddEmployee(EmployeeArray)
        case '2':
            Functions.UpdateEmployeeAttributes(EmployeeArray, EmployeeVacationArray, EmployeeExperienceArray)
        case '3':

            Functions.AddUpdateAdministrative(EmployeeArray, EmployeeVacationArray)
        case '4':

            Functions.AddUpdateAcademic(EmployeeArray, EmployeeExperienceArray)
        case '5':

            Functions.EmployeeStatistics(EmployeeArray)
        case '6':

            Functions.SalaryStatistics(EmployeeArray)
        case '7':

            Functions.RetirementInformation(EmployeeArray)
        case '8':

            Functions.CoursesStatistics(EmployeeArray, EmployeeExperienceArray)
        case '9':
            Functions.AdministrativeStatistics(EmployeeVacationArray, EmployeeArray)
        case '10':

            Functions.AcademicStatistics(EmployeeArray, EmployeeExperienceArray)
        case '11':
            '''Print All Lists'''
            print("Employee List:-\n")
            for i in EmployeeArray.items():
                print(i)
            print("Employee Vacation List:-\n")
            for i in EmployeeVacationArray.items():
                print(i)
            print("Employee Experience List:-\n")
            for i in EmployeeExperienceArray.items():
                print(i)
        case '0':
            '''Exit'''
            exit(0)
        case _:
            print("Invalid Command")
            exit(0)
