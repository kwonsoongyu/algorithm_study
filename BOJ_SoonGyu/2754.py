import sys
input = sys.stdin.readline

grade = input().rstrip()

if grade == "A+":
    print(4.3)
if grade == "A0":
    print(4.0)
if grade == "A-":
    print(3.7)
if grade == "B+":
    print(3.3)
if grade == "B0":
    print(3.0)
if grade == "B-":
    print(2.7)
if grade == "C+":
    print(2.3)
if grade == "C0":
    print(2.0)
if grade == "C-":
    print(1.7)
if grade == "D+":
    print(1.3)
if grade == "D0":
    print(1.0)
if grade == "D-":
    print(0.7)
if grade == "F":
    print(0.0)
