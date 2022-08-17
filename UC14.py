# Ability to get the Total Wage when queried by Company

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
        self.return_value = self.wageCount()

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
        # print(company_details_list)
        print("Total employee wage of the month : ", company_details_list[len(company_details_list)-1])
        return company_details_list

if __name__ == "__main__":
    condition = True
    company_details_list_array = []
    while(condition == True):
        # print("")
        print("  Welcome To Employee Payroll Form!!  ")
        choice = int(input("1. Enter 1 to add Company Details \n2. Enter 2 to know about existing Company Details \n3. Exit \n"))

        if(choice == 1):
            company_name = input("Enter Name of the Company : ")
            wage_per_hour = int(input("Enter Wage Per Hour : "))
            days_per_month = int(input("Enter Working Days Per Month : "))
            max_total_working_hrs = int(input("Enter Maximum Working Hours Per Month : "))
            employeePayroll = EmployeePayroll(company_name, wage_per_hour, days_per_month, max_total_working_hrs)
            company_details_list_array.append(employeePayroll.return_value)

        elif(choice == 2):
            company = input("Enter Company name to find Employee Wage details : ")
            for company_details in company_details_list_array:
                if(company in company_details):
                    print("Company Name : ", company_details[0],
                          "\nWage Per Hour : ", company_details[1],
                          "\nWorking Days Per Month : ", company_details[2],
                          "\nMaximum Working Hours Per Month : ", company_details[3],
                          "\nTotal Employee Wage per Month: ", company_details[4])

        else:
            condition = False