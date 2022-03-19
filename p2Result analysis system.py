#Result analysis system
name=input('Enter your  Name :')
rollnum=int(input('Enter your Rollno :'))
branch=input('Enter your branch :')
clas=input('Enter your class :')
mailid=input('Enter your Emailid:')


s1=input('Enter first subject name :')
print("Enter",s1,"marks:",end="")
s1=int(input(':'))
s2=input('Enter second subject name :')
print("Enter",s2,"marks:",end="")
s2=int(input(':'))
s3=input('Enter third subject name :')
print("Enter",s3,"marks:",end="")
s3=int(input(':'))

if rollnum>=1 and rollnum<=20 :
    e1=int(input("Enter  ETHICS IN IT marks  "))
    total=s1+s2+s3+e1
    per=(total)*100/400
elif rollnum>=20 and rollnum<=40 :
    e2=int(input("Enter  UHV marks "))
    total=s1+s2+s3+e2
    per=(total)*100/400
elif rollnum>=40 and rollnum<=50 :
    e3=int(input("Enter the Environment studies marks "))
    total=s1+s2+s3+e3
    per=(total)*100/400
 
 #Result grade
if(per>=90):
    print('Result analysis of: ',name) 
    print('Total marks =',total)
    print('Percentage = ',per,'%')
    print('Grade A') 
elif(per>=80,per<90):
    print('Result analysis of: ',name)
    print('Total marks =',total)
    print('Percentage = ',per,'%')
    print('Grade B')
elif(per>=70,per<80):   
    print('Result analysis of: ',name)
    print('Total marks =',total)
    print('Percentage = ',per,'%')
    print('Grade C')
elif(per>=60,per<70):
    print('Result analysis of: ',name)
    print('Total marks =',total)
    print('Percentage = ',per,'%')
    print('Grade D')
else:
    print('Result analysis of: ',name)
    print('Total marks =',total)
    print('Percentage = ',per,'%')
    print('Grade E')
    

 
