# Calculate Wages till a condition of total working hours or days is reached for
# a month - Assume 100 hours

import random

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

while (DAY_COUNT <= DAYS_PER_MONTH | TOTAL_EMP_HRS <= MAX_TOTAL_WORKING_HOURS):
    EMP_CHECK = random.randint(0, 2)
    if (EMP_CHECK == IS_ABSENT):
        EMP_HOURS = 0
    elif (EMP_CHECK == IS_PRESENT):
        EMP_HOURS = 8
    else:
        EMP_HOURS = 4

    DAY_COUNT = DAY_COUNT + 1
    EMP_WAGE = WAGE_PER_HOUR * EMP_HOURS
    TOTAL_EMPWAGE += EMP_WAGE
    TOTAL_EMP_HRS += EMP_HOURS
    print("Total Employee Wage of the day : ", TOTAL_EMPWAGE)

print("Total employee wage of the month : ", TOTAL_EMPWAGE)