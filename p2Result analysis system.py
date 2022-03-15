#Result analysis system
name=input('Enter ur  Name:')
rollnum=int(input('Enter ur Roll no:'))
clas=input('Enter ur class:')
mailid=input('Enter ur Email id:')

print('Sub\t\t\t\t\t\tMarks(out of 100)')
phy=int(input('Physics\t\t\t\t\t\t'))
chem=int(input('Chemistry\t\t\t\t\t'))
bio=int(input('Biology\t\t\t\t\t\t'))
M1=int(input('Maths\t\t\t\t\t\t'))
total=phy+chem+bio+M1
avg=(phy+chem+bio+M1)/4

print('Total Marks:\t\t\t\t\t',total)
per=total/400*100 
print('Percentage\t\t\t\t\t',per,'%')
if(avg>=90):
    print('You pass with A grade')
elif(avg>=80,avg<90):
    print('You passed with B grade')
elif(avg>=70,avg<80):   
    print('You passed with C grade')
elif(avg>=60,avg<70):
    print('You passed with D grade')
else:
    print('Grade F')
    

 
