subjects = ["Maths","Science","English","History","Tamil"]

marks=[]

for subject in subjects:
    mark= int(input("Enter Your marks:-"))
    marks.append(mark)

print("subject marks ")

for i in range(len(subjects)):
    if marks[i]>50:
        print(subjects[i])

count= 0
for mark in marks:
    if mark>=40:
        count +=1
print("which subject is greater than or equal 40:", count)

totalMarks= sum(marks)
avarageMarks = totalMarks / len(subjects)
print("Total marks:", totalMarks)
print("average marks:", avarageMarks)

if avarageMarks>45:
    print("pass the exam")
else:
    print("Redo a exam ")

maxMarks= max(marks)
maxIndex= marks.index(maxMarks)
print("highest marks subject is", subjects[maxIndex])