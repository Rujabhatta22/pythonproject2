#A school decided to replace the desks in three classroom. Each desk sits two students.
#given the number of students in each class, print the smallest possible number of desk that can be purchased.
#the program should read three integers: the number of students in each of the three classes, a, b and c respectively.
#In the first test there are three groups. The first group has 20 students and thus needs 10 desks.
#The second group has 21 students, so they can by with no fewer than 11 desks. 11 desks are also enough for the third group of 22 students. so, we need 32 desks in total.

no_student_class1=int(input("enter the number of students in first class:"))
no_student_class2=int(input("enter the number of students in second class:"))
no_student_class3=int(input("enter the number of students in third class:"))
desk_class1=(no_student_class1//2)
print(f"the required number of desk for first class is {desk class1}")
desk_class2=(no_student_class2//2)
print(f"the required number of desk for second class is {desk class2}")
desk_class3=(no_student_class3//2)
print(f"the required number of desk for third class is {desk class3}")
remain_class1= (no_student_class1%2)
print(f"remaining desk of first class is {remain_class1}")
remain_class2= (no_student_class2%2)
print(f"remaining desk of second class is {remain_class2}")
remain_class3= (no_student_class3%2)
print(f"remaining desk of third class is {remain_class3}")
total_desk= desk_class1 + desk_class2 + desk_class3 + remain_class1 + remain_class2 + remain_class3
print(f"total number of desk that can be purchased is {total_desk}")




