import json
class dataBase:
    def __init__(self, path):
        self.path = path

    def readDataBase(self):
        """
        This method is used to read the whole data base.
        :return: dictFromJson - dict object that represents the whole data base
        """
        with open(self.path, "r") as file:
            dictFromJson = json.load(file)
        return dictFromJson

    def writeDataBase(self, newInfo):
        """
        This method is used to write the data base.
        First, you modify the exact data that you want modified and when you write the data base,
        you have to input the whole new data base.
        :param newInfo: - dict - the new data base.
        :return: None
        """
        with open(self.path, "w") as file:
            json.dump(newInfo, file, indent=4)

class Employee:
    global DB
    DB = dataBase("employees.json")

    global read
    read = DB.readDataBase()

    def __init__(self):
        self.lastName = str()
        self.firstName = str()
        self.salary = float()
        self.jobPosition = str()
        self.skillLevel = str()

    def addEmployee(self, lastName, firstName, salary, jobPosition, skillLevel):
        """
        This method is used to add a new employee in employees file.
        :param lastName: - string - Employee's last name
        :param firstName: - string - Employee's first name
        :param salary: - float - Employee's salary
        :param jobPosition: - string - Employee's job position
        :param skillLevel: - string - Employee's skill level
        :return: None
        """
        self.lastName = lastName
        self.firstName = firstName
        self.salary = salary
        self.jobPosition = jobPosition
        self.skillLevel = skillLevel
        read["Employees"].append({"Last Name": self.lastName, "First Name": self.firstName, "Salary": self.salary, "Job Position": self.jobPosition, "Skill Level": self.skillLevel})

        DB.writeDataBase(read)

    def changeSalary(self, lastName, firstName, newSalary):
        """
        This method is used to change the employee's salary.
        :param lastName: - string - Employee's last name
        :param firstName: - string - Employee's first name
        :param newSalary: - float - - string - Employee's new salary
        :return: None
        """
        flag = 0
        for employee in read['Employees']:
            if employee["Last Name"] == lastName:
                if employee["First Name"] == firstName:
                    flag = 1
                    self.salary = newSalary
                    employee["Salary"] = newSalary
                    DB.writeDataBase(read)
                    print(employee["Last Name"] + " " + employee["First Name"] + "'s salary has been changed.")

        if flag == 0:
            print("Employee not found.")

    def changeJobPosition(self, lastName, firstName, newJobPosition):
        """
        This method is used to change the employee's job position.
        :param lastName: - string - Employee's last name
        :param firstName: - string - Employee's first name
        :param newSalary: - string - - string - Employee's new job position
        :return: None
        """
        flag = 0
        for employee in read['Employees']:
            if employee["Last Name"] == lastName:
                if employee["First Name"] == firstName:
                    flag = 1
                    self.jobPosition = newJobPosition
                    employee["Job Position"] = newJobPosition
                    print(employee["Last Name"] + " " + employee["First Name"] + "'s job position has been changed.")
                    DB.writeDataBase(read)

        if flag == 0:
            print("Employee not found.")

    def changeSkillLevel(self, lastName, firstName, newSkillLelvel):
        """
        This method is used to change the employee's skill level.
        :param lastName: - string - Employee's last name
        :param firstName: - string - Employee's last name
        :param newSkillLelvel: - string - Employee's new skill level
        :return: None
        """
        flag = 0
        for employee in read['Employees']:
            if employee["Last Name"] == lastName:
                if employee["First Name"] == firstName:
                    flag = 1
                    self.skillLevel = newSkillLelvel
                    employee["Skill Level"] = newSkillLelvel
                    print(employee["Last Name"] + " " + employee["First Name"] + "'s skill level has been changed.")
                    DB.writeDataBase(read)

        if flag == 0:
            print("Employee not found.")

    def deleteEmployee(self, lastName, firstName):
        """
        This method is used to delete an employee from employees file.
        :param lastName: - string - Employee's last name
        :param firstName: - string - Employee's last name
        :return: None
        """
        self.lastName = str()
        self.firstName = str()
        self.salary = float()
        self.jobPosition = str()
        self.skillLevel = str()
        
        for i in range(0, len(read['Employees'])):
            if read['Employees'][i]["Last Name"] == lastName:
                if read['Employees'][i]["First Name"] == firstName:
                    read['Employees'].remove(read['Employees'][i])
                    break
        DB.writeDataBase(read)
    def getEmployees(self):
        """
        :return: - list - last and first names of all employees
        """
        employeeList = []
        for employee in read['Employees']:
            employeeList.append(employee['Last Name'] + " " + employee["First Name"])

        return employeeList

    def getDetails(self, lastName, firstName,):
        """
        :param lastName: - string - Employee's last name
        :param firstName: - string - Employee's first name
        :return: - string - All details about the employee.
        """
        for employee in read['Employees']:
            if employee["Last Name"] == lastName:
                if employee["First Name"] == firstName:
                    return "Last name: " + employee["Last Name"] + ", First Name: " + employee["First Name"] + ", Salary: " + str(employee["Salary"]) + ", Job Position: " + employee["Job Position"] + ", Skill Level: " + employee["Skill Level"]
        return "Employee not found."

e = Employee()

print(e.getEmployees())
print()
e.addEmployee("Balan", "Andrei", 2500, "Engineer", "Junior")
print(e.getEmployees())
print(e.getDetails("Balan", "Andrei"))
e.changeSalary("Balan", "Andrei", 3000)
print(e.getDetails("Balan", "Andrei"))
e.changeJobPosition("Balan", "Andrei", "Automation Tester")
print(e.getDetails("Balan", "Andrei"))
e.changeSkillLevel("Balan", "Andrei", "mid")
print(e.getDetails("Balan", "Andrei"))
e.deleteEmployee("Balan", "Andrei")
print(e.getEmployees())