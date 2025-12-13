# #Q1:basic calculator
# print("==MY FIRST PROJECT==")
# print('  \n =+= BASIC CALCULATOR=+=\n   ')
# while True:
#  a=float(input('ENTER NUM 1='))
#  b=float(input('ENTER NUM 2='))
#  print("CHOOSE 1='+'.\n2='*'.\n3='-'.\n4='/'.")
#  ch=int(input('Enter choice='))

#  if ch == 1:
#     print('sum=',a + b)
#  elif ch == 2:
#     print('sum=',a * b)
#  elif ch == 3 :
#     print('sum=',a - b)
#  elif ch == 4:
#     print('sum=',a / b)
#  else:
#     print('Invalid')
 

# Q2
# temp converter
# print('Temperture Converter')
# print('1.F=C OR 2.C=F')
# op=int(input('enter your choice='))
# if op == 1:
#     f=float(input('enter f='))
#     c=(f-32)*9/5
#     print("c=",c)
# elif op == 2:
#     c=float(input('enter your c='))
#     f=(c*9/5)+32
#     print("f=",f)
# 
# Q3
# print('leap year checker')
# i=int(input('enter the year='))
# if i % 400 == 0:
#     print('leap year')
# elif i % 100==0:
#     print('not leap year')
# elif i % 4==0:
#     print('leap year')
# else:
#     print('not leap year')

# Q4
# print('factorial finder')
# n=int(input('enter num='))
# fact=1
# for i in range(1,n+1):
#     fact*=i
#     print(fact)

# Q5
# print('table finder')
# n=int(input('entre table='))
# for i in range(1,11):
#     o=n * i
#     print(n ,"*",i ,"==",o )

# Q6
# print('EVEN OR ODD')
# i=int(input('enter num='))
# if (i  % 2)==0:
#     print('even')
# else:
#     print('odd')

# Q7
# print('Simple interest finder')
# p=float(input('enter invest='))
# r=float(input('enter the rate='))
# t=float(input("enter the time="))
# i=(p*r*t)/100
# print('interest=',i)

# Q8
# print('BMI finder')
# w=float(input('enter weight='))
# h=float(input('enter height='))
# o=w/ (h * h)
# if o <= 18.5 :
#     print('underweight')
# elif o >=18.5 and o<=24.9:
#     print('normalweight')
# elif o>=25 and o<=29.9:
#     print('overweight')
# else:
#     print('obese')
# print(o)

# Q9
# print('pos,neg,even,odd,sq finder')
# while True:
#     i=int(input('enter='))
#     if i > 0:
#         print('positive')
#     elif i <0:
#         print('negative')
#     if i %2==0:
#         print('even=',i)
#     elif i==0:
#         print('zero')
#     if ( i**0.5)**2 == i:
#         print('perfect sqaure')
#     else:
#         print('odd')

# Q10
# print('Grade and percentage Finder')
# s1=float(input('enter s1='))
# s2=float(input('enter s2='))
# s3=float(input('enter s3='))
# s4=float(input('enter s4='))
# s5=float(input('enter s5='))
# s6=float(input('enter s6='))
# t=(s1+ s2+s3+s4+s5+s6)/6
# if t >90:
#     print('A++ GRADE')
# elif t < 90 and t > 85:
#     print('A GRADE')
# elif t < 85 and t>75:
#     print('B GRADE')
# elif t <75 and t >50:
#     print('C GRADE')
# elif t <50 and t > 35:
#     print('D GRADE ')
# else:
#     print('Fail')

# print('percentage=',t)