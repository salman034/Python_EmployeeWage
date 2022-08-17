# Add Part time Employee & Wage

import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 4

IS_ABSENT = 0
IS_PRESENT = 1
IS_PART_TIME = 2

EMP_Check = random.randint(0, 2)
if(EMP_Check == IS_ABSENT):
    print("Employee is Absent")
    print("Daily Employee Wage : ", 0)
elif(EMP_Check == IS_PRESENT):
    print("Employee is Present")
    print("Daily Employee Wage : ", WAGE_PER_HOUR * FULL_DAY_HOUR)
else:
    print("Employee is working Part Time")
    print("Daily Employee Wage : ", WAGE_PER_HOUR * PART_TIME_HOUR)