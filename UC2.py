# Calculate Daily Employee Wage

import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8

EMP_CHECK = random.randint(0, 1)
if(EMP_CHECK == 0):
    print("Employee is Absent")
    print("Daily Employee Wage : ", 0)
else:
    print("Employee is Present")
    print("Daily Employee Wage : ", WAGE_PER_HOUR * FULL_DAY_HOUR)