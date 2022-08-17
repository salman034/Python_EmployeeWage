# Calculating Wages for a Month

import random

WAGE_PER_HOUR = 20
DAYS_PER_MONTH = 20

IS_ABSENT = 0
IS_PRESENT = 1
IS_PART_TIME = 2


DAY_COUNT = 1
EMP_HOURS = 0
TOTAL_EMPWAGE = 0
EMP_WAGE = 0

while (DAY_COUNT <= DAYS_PER_MONTH):
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
    print("Total Employee Wage of the day : ", TOTAL_EMPWAGE)

print("Total employee wage of the month : ", TOTAL_EMPWAGE)