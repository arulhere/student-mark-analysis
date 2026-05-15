'''
    ------------------------------------
        STUDENT MARK ANALYSIS
    ------------------------------------
    1.AVERAGE BY SUBJECT AND STUDENT
    2.HIGHEST & LOWEST PER SUBJECT
    3.OVERALL CLASS TOPPER
    4.PASS COUNT PER SUBJECT
    5.WHUCH SUBJECT IS DIFFICULT?
    6.RANKING STUDENTS
    -------------------------------------
'''

import numpy as np

np.random.seed(40)
marks=np.random.randint(10,101,size=(20,6))

average_by_subject=np.mean(marks,axis=0)
average_by_student=np.mean(marks,axis=1)

highest=np.max(marks,axis=0)
lowest=np.min(marks,axis=0)

total_marks=np.sum(marks,axis=1)

pass_count_per_subject=marks>=40
pass_count=np.sum(pass_count_per_subject,axis=0)

rank=np.argsort(-total_marks)+1
print("Average by Subject",average_by_subject)
print("Average by Student",average_by_student)
print("Highest marks by subject",highest)
print("Lowest marks by subject",lowest)

print("Class topper is roll no",np.argmax(total_marks),"with the mark of",np.max(total_marks))

print("Pass count by subject",pass_count)

print("Difficult subject is",np.argmin(average_by_subject)+1,"with the average of",np.min(average_by_subject))

print("Rank of the students is",rank[::])