"""
EXERCISE 01 - Grade calculator
Topic: if / elif / else

TASK
----
Given a marks value, print the grade using this scale:
    90 and above  -> A
    75 to 89      -> B
    60 to 74      -> C
    40 to 59      -> D
    below 40      -> F

Then test it with several different marks values.

EXPECTED OUTPUT (for the values already listed below)
----------------------------------------------------
95 -> A
82 -> B
72 -> C
55 -> D
30 -> F
"""




marks = [95, 82, 72, 55, 30]

for mark in marks:
    if mark >= 90:
        grade = "A"
    elif mark >= 75:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 40:
        grade = "D"
    else:
        grade = "F"

    print(mark, "->", grade)
