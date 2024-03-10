a=int(input("Enter your mark : "))
if a>=0 and a<=32:
    print("Failed")
elif a>=33 and a<40:
    print("D")
elif a>=40 and a<50:
    print("C")
elif a>=50 and a<60:
    print("B")
elif a>=60 and a<70:
    print("A-")
elif a>=70 and a<80:
    print("A")
elif a>=80 and a<=100:
    print("A+")
else:
    print("Invalid Input")


