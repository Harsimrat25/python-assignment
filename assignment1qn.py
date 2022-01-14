#1:

x=int(input("Enter number in x: "))
y=int(input("Enter number in y: "))
z=int(input("Enter number in z: "))

print("Value of x is :",x)
print("Value of y is :",y)
print("Value of z is :",z)

avg=(x+y+z)/3

print("Average of given numbers is :",avg)


#2:
#amount is in dollars
GI=float(input("Enter the gross income"))
dep=int(input("Enter the number of dependents"))
rate=0.2 #20percent
stndDed=10000

taxableInc=GI-stndDed-(dep*3000)
tax=taxableInc*rate

print("tax is",tax)


#3:
#[SID,Name,Gender,Branch,CGPA]
student=[21104115,"Harsimrat Gill","F","Electrical Engineering",8.0]
print(student)


#4:
#marks of a student in 5 subjects
marks=[59,98,78,87,86]
marks.sort()
print(marks)



#5.a:
colour=["Red","Green","White","Black","Pink","Yellow"]
colour.pop(3)
print(colour)

#5.b:
colour=["Red","Green","White","Black","Pink","Yellow"]
#replacing Black and Pink with Purple
colour[3]=colour[4]="Purple" #removing extra purple
colour.pop(4)
print(colour)









