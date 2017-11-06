'''
Trimark Utility
Copyright (C) Ketsu8, 2017 – 2018.

This utility allows you to know your approximate
trimester rating. You must enter numbers, and the
program after each input computes your estimate
by the average aremetic from the sum of the estimates.
Also, all numbers are rounded to the tenth.

Read me on GitHub: http://github.com/Ketsu8/
'''
isRound = True #turn on round mark (by default it's on)

import math
print("Starting TrimesterMark...")
count = 0
trimesterMark = 0
while True:
    marks = int(input("Input your mark here: "))
    if marks > 5:
        print("Int " + str(marks) + " bigger then five.")
    elif marks < 2:
        print("Int must be bigger then two.")
    else:
        count += 1
        trimesterMark += marks
        if isRound:
            print("Now mark: " + str(round(trimesterMark / count, 1)) + ".")
        else:
            print("Now mark: " + str(trimesterMark / count) + ".")
