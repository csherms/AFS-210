class Employee:
    def __init__(self, firstName,lastName,employeeId,salary,totalHours):
       self.firstName = input("Enter first name: ")
       self.lastName = input("Enter last name: ")
       self.employeeId = int(input("Enter employee ID: "))
       self.salary = float(input("Enter hourly wage: "))
       self.totalHours = float(input("Enter hours worked: "))
       
    def pay(self):
     if self.totalHours <= 40:
      totalPay =  self.totalHours * self.salary
      print(self.firstName, self.lastName + "'s", "Pay is ", totalPay)
     else:
       # print(self.firstName, self.lastName + "'s", "Pay is ", (self.totalHours * self.salary) * 1.5)
       totalPay = self.totalHours * self.salary
       hoursDifference = self.totalHours - 40
       overTimePay = hoursDifference * 1.5
       totalPayWithOverTime = totalPay + overTimePay
       print(self.firstName, self.lastName + "'s", "Total pay with overtime is ", totalPayWithOverTime)
       
       
emp1 = Employee(str, str, int, float, float)
Employee.pay(emp1)
       
