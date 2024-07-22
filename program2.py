def add(n1,n2):
 return n1+n2
def sub(n1,n2):
 return n1-n2
def mul(n1,n2):
 return n1*n2
def div(n1,n2):
 return n1/n2
print("please select an operation")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
print("5.exit")
while True:
 choice=input("enter your choice (1/2/3/4/5):")
 if (choice=='5'):
  print("goodbye")
  break

 if choice in ('1','2','3','4'):
 
  n1=float(input("enter first number: "))
  n2=float(input("enter second number: "))
  if choice=='1':
   print(n1,"+",n2,"=",add(n1,n2))
  elif choice=='2':
   print(n1,"-",n2,"=",sub(n1,n2))
  elif choice=='3':
   print(n1,"*",n2,"=",mul(n1,n2))
  elif choice=='4':
   print(n1,"/",n2,"=",div(n1,n2))

else:	
 print("invalid input")
