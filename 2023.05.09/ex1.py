"""• Assume you have following subjects. Namely Programming, Database, Networking and Professional Practice. Create an array to store these 4 subjects.

Thereafter, get the marks for these subjects from user and store the marks in an array. You're expected to use for loop to receive the marks from user

Once you do so, you are expected to do the following

1) Output the subjects and marks using for loop

2) Consider 60 or above 60 as the pass marks. a. Calculate the Number of subjects passed.

3) Dynamically assign the passed subjects to the array passedSubjects and failed subjects to falledSubjects so do passedSubjectMarks and falledSubjectMarks

4) Output the passedSubjects and failedSubjects using for loop

5) Output the total marks and average marks of passed subjects 

6) Output the total marks and average marks of failed subjects"""


#creat 4 arrays 
subjects=["Programing","Databace","networking","profossional practice"]

#this empty array store a marks
marks = []
#getting user input 
for i in range (len(subjects)):
    SubjectMarks= int(input("Enter your subject Marks:-"))
    marks.append(SubjectMarks)

print("Subject and Marks")
for i in range(len(subjects)):
    print(subjects[i],marks[i])

#Number of pass and fill subjects
noofPass=0
for mark in marks:
    if mark>=60:
        noofPass+=1

#dinamicaly store arrays 
passedsubjects= []
passedsubjectsmarks= []
failsubject=[]
failsubjectMarks=[]

for i in range(len(subjects)):
    if marks[i] >=60:
        passedsubjects.append(subjects[i])
        passedsubjectsmarks.append(marks[i])
    else:
        failsubject.append(subjects[i])
        failsubjectMarks.append(marks[i])

print("Passed Subjects ")
for i in range(len(passedsubjects)):
    print(passedsubjects[i],passedsubjectsmarks[i])

print("fail subject marks")    
for i in range(len(failsubject)):
    print(failsubject[i],failsubjectMarks[i])

totalPassedmarks=sum(passedsubjectsmarks)
avragePassMarks= totalPassedmarks / len(passedsubjectsmarks)

print("Total Marks for pass SUbjects:",totalPassedmarks)
print("average Marks for Pass Subject:",avragePassMarks)


totalfailmarks=sum(failsubjectMarks)
avragefailmarks= totalfailmarks / len(failsubjectMarks)

print("failSubject marks:",totalfailmarks)
print("average marks for fail subject:",avragefailmarks)