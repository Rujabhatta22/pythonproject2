#n students take K apples and distribute them among each other evenly.
# the remaining (the unidivisibale) part remains in the basket.
# How many apples will each single student get?
# This program reads the number N and K.
# it should print the two number for the question above.

N=int(input("enter the number of student in class"))
k=int(input("enter the number of apples"))
apples_get = (k//N)
remaining_apples=(k%N)
print(f"enter student got {apples_get}")
print(f"the remaining apples are {remaining_apples}")