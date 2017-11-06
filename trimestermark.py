'''
TrimesterMark
Copyright (C) 2017. Ketsu8.
'''
isRound = True #turn on round mark

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
