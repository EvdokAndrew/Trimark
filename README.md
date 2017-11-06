# Trimark Utility
The Trimark utility allows you to know your approximate trimester rating. You must enter numbers, and the program after each input computes your estimate by the average aremetic from the sum of the estimates. Also, all numbers are rounded to the tenth.
### How to use it?
After each input of numbers, the average score obtained is displayed.
```
python3 trimestermark.py 
Starting TrimesterMark...
Input your mark here: 5
Now mark: 5.0.
Input your mark here: 4
Now mark: 4.5.
Input your mark here: 3
Now mark: 4.0.
Input your mark here: 
```
The code for obtaining the arithmetic mean from the entered estimates:
```python
count += 1
trimesterMark += marks
print("Now mark: " + str(trimesterMark / count) + ".")
```
