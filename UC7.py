# Refactor the Code to write a Class Method to Compute Employee Wage - Use Class Method and Class

import random

class EmployeeWage():
    WAGE_PER_HOUR = 20
    DAYS_PER_MONTH = 20
    MAX_TOTAL_WORKING_HOURS = 100

    IS_ABSENT = 0
    IS_PRESENT = 1
    IS_PART_TIME = 2

    DAY_COUNT = 1
    EMP_HOURS = 0
    TOTAL_EMPWAGE = 0
    EMP_WAGE = 0
    TOTAL_EMP_HRS = 0

    def WageCount(self):
        while self.DAY_COUNT <= self.DAYS_PER_MONTH and self.TOTAL_EMP_HRS <= self.MAX_TOTAL_WORKING_HOURS:
            EmpCheck = random.randint(0, 2)
            if (EmpCheck == self.IS_ABSENT):
                self.EMP_HOURS = 0
            elif (EmpCheck == self.IS_PRESENT):
                self.EMP_HOURS = 8
            else:
                self.EMP_HOURS = 4

            self.DAY_COUNT = self.DAY_COUNT + 1
            self.EMP_WAGE = self.WAGE_PER_HOUR * self.EMP_HOURS
            self.TOTAL_EMPWAGE += self.EMP_WAGE
            self.TOTAL_EMP_HRS += self.EMP_HOURS
            print("Total Employee Wage of the day : ", self.TOTAL_EMPWAGE, " Day No : ", self.DAY_COUNT - 1)

        print("Total employee wage of the month : ", self.TOTAL_EMPWAGE)

empWage = EmployeeWage()
empWage.WageCount()