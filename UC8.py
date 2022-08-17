# Compute Employee Wage for multiple companies.

import random

class EmployeePayroll():

    IS_ABSENT = 0
    IS_PRESENT = 1
    IS_PART_TIME = 2

    DAY_COUNT = 1
    EMP_HOURS = 0
    TOTAL_EMPWAGE = 0
    EMP_WAGE = 0
    TOTAL_EMP_HRS = 0

    def __init__(self, Company_Name, WAGE_PER_HOUR, DAYS_PER_MONTH, MAX_TOTAL_WORKING_HOURS):

        self.Company_Name = Company_Name
        self.WAGE_PER_HOUR = WAGE_PER_HOUR
        self.DAYS_PER_MONTH = DAYS_PER_MONTH
        self.MAX_TOTAL_WORKING_HOURS = MAX_TOTAL_WORKING_HOURS

    def wageCount(self):

        print("<============================================================================================>")
        while self.DAY_COUNT <= self.DAYS_PER_MONTH and self.TOTAL_EMP_HRS <= self.MAX_TOTAL_WORKING_HOURS:
            empCheck = random.randint(0, 2)
            if (empCheck == self.IS_ABSENT):
                self.EMP_HOURS = 0
            elif (empCheck == self.IS_PRESENT):
                self.EMP_HOURS = 8
            else:
                self.EMP_HOURS = 4

            self.DAY_COUNT = self.DAY_COUNT + 1
            self.EMP_WAGE = self.WAGE_PER_HOUR * self.EMP_HOURS
            self.TOTAL_EMPWAGE += self.EMP_WAGE
            self.TOTAL_EMP_HRS += self.EMP_HOURS
            print("Employee Wage of the day : ", self.EMP_WAGE,
                  " Total Employee Wage upto the Day : ", self.TOTAL_EMPWAGE, " Day No : ", self.DAY_COUNT - 1)

        company_details_list = [self.Company_Name, self.WAGE_PER_HOUR,
                                self.DAYS_PER_MONTH, self.MAX_TOTAL_WORKING_HOURS, self.TOTAL_EMPWAGE]
        print(company_details_list)
        print("Total employee wage of the month : ", company_details_list[len(company_details_list)-1])

employeePayroll1 = EmployeePayroll("Accenture", 50, 23, 187)
employeePayroll1.wageCount()

employeePayroll2 = EmployeePayroll("Google", 60, 20, 198)
employeePayroll2.wageCount()