# Employee Class
class EmployeeClass:
    def __init__(self, ID, FName, MName, LName, DateOfBirth, MartialStatus, NumberOfChildren, Gender, EContact,
                 PContact, HContact, Type,
                 Status,
                 Department, StartingTime, BasicSalary, HealthInsurance):
        self.ID = ID
        self.FName = FName
        self.MName = MName
        self.LName = LName
        self.DateOfBirth = DateOfBirth
        self.MartialStatus = MartialStatus
        self.NumberOfChildren = NumberOfChildren
        self.Gender = Gender
        self.EContact = EContact
        self.PContact = PContact
        self.HContact = HContact
        self.Type = Type
        self.Status = Status
        self.Department = Department
        self.StartingTime = StartingTime
        self.BasicSalary = BasicSalary
        self.HealthInsurance = HealthInsurance

    def PrintEmployee(self):
        print(
            f"{self.ID}; {self.FName} {self.MName} {self.LName}; {self.DateOfBirth}; {self.MartialStatus}; {self.NumberOfChildren}; {self.Gender}; {self.EContact}, {self.PContact}, {self.HContact}; {self.Type}; {self.Status}; {self.Department}; {self.StartingTime}; {self.BasicSalary}; {self.HealthInsurance}")

    def __str__(self):
        return f"{self.ID}; {self.FName} {self.MName} {self.LName}; {self.DateOfBirth}; {self.MartialStatus}; {self.NumberOfChildren}; {self.Gender}; {self.EContact}, {self.PContact}, {self.HContact}; {self.Type}; {self.Status}; {self.Department}; {self.StartingTime}; {self.BasicSalary}; {self.HealthInsurance}"


# Vacation Class
class VacationClass(EmployeeClass):
    def __init__(self, ID, FName, MName, LName, DateOfBirth, MartialStatus, NumberOfChildren, Gender, EContact,
                 PContact, HContact, Type,
                 Status,
                 Department, StartingTime, BasicSalary, HealthInsurance, Vacation):
        super().__init__(ID, FName, MName, LName, DateOfBirth, MartialStatus, NumberOfChildren, Gender, EContact,
                         PContact, HContact, Type,
                         Status,
                         Department, StartingTime, BasicSalary, HealthInsurance)
        self.Vacation = Vacation

    def PrintVacation(self):
        self.PrintEmployee()
        for v in self.Vacation:
            print(v)

    def __str__(self):
        return self.Vacation


# Experiance Class
class ExperianceClass(EmployeeClass):
    def __init__(self, ID, FName, MName, LName, DateOfBirth, MartialStatus, NumberOfChildren, Gender, EContact,
                 PContact, HContact, Type,
                 Status,
                 Department, StartingTime, BasicSalary, HealthInsurance, Experience):
        super().__init__(ID, FName, MName, LName, DateOfBirth, MartialStatus, NumberOfChildren, Gender, EContact,
                         PContact, HContact, Type,
                         Status,
                         Department, StartingTime, BasicSalary, HealthInsurance)
        self.Experience = Experience

    def PrintExperiance(self):
        self.PrintEmployee()
        for ex in self.Experience:
            print(ex)

    def __str__(self):
        return self.Experience
