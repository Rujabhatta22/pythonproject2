#Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes are displayed on the 24th digital clock?
#the program should print two number: the number of hours (between 0 and 23) and the number of minutes (between 0 and 59)
#for example, if N=150, then 150 minutes have passed since midnight. i.e. now is 2:30 am. So, the program should print 2:30.

N=int(input("enter the minutes passed since midnight"))
hours=(N//60)
minute=(N%60)
print(f"the hours is {hours}")
print(f"the minutea is {minutes}")
print(f"its {hours}:{minutes} now")