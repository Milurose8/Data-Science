s1=float(input("Enter the side 1 of the triangle\n"))
s2=float(input("Enter the side 2 of the triangle\n"))
s3=float(input("Enter the side 3 of the triangle\n"))
if(s1==s2 and s2==s3):
    print("Equilateral Triangle")
elif(s1==s2 or s2==s3 or s3==s1):
    print("Isosceles triangle")
else:
    print("scalen Triangle")