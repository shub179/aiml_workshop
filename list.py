marks=[]
for i in range(10):
    mk=int(input("Enter the marks for 10 students:"))
    marks.append(mk)
print(marks)
marks[4]=25
print("updated marks",marks)
for i in marks:
    if marks>15:
        print(marks)