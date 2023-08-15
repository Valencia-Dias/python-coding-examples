# The __init__() function is called automatically every time the class is being used to create a new object.
class Employee:
    def __init__(self, name, empId):
        self.empName = name
        self.employeeId = empId



e = Employee('Val', 2)
print(e.empName)
print(e.employeeId)
