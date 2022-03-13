#Check Input value is palindrome
a=int(input('Enter the number'))
a1=a
#calculate reverse of th no.
rev=0
while(a>0):
    t=a%10
    rev=rev*10+t
    a=a//10
if (a1==rev):
  print('Number is palindrome')
else:
    print('Number is not palndrome')        