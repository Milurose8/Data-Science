a=int(input("Enter no:1 \n"))
b=int(input("Enter no:2 \n"))
for i in range (1,a):
    if(a%i==0 and b%i==0):
        hcf=i
if(hcf==1):
    print("coprime")
else:
    print("not coprime")
