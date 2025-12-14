#   Q1:extend()
# list=[1,2,3,2,4,2]
# list.extend([34,2,32,55])
# print(list)

# Q2:;zip()
# a=[1,2,3]
# b=["a","b","c"]
# print(list(zip(a,b)))

# # Q3:: Arm strong
# n=int(input('enter num='))
# d=len(str(n))
# t=sum(int(c)**d for c in str(n))
# if t == n:
#     print('armstrong=',n)
# else:
#     print('not armstrong=',n)

# Q4:: prime or not
# while True:
#     n=int(input('enter='))
#     print("prime" if n >1 and all(n % i !=0 for i in range(2,int(n**0.5)+1) ) else "not prime")

# Q5 :: GCD
# a=int(input('enter a='))
# b=int(input('enter b='))
# while b != 0:
#     a,b=b,a%b
#     print('GCD=',a)

# Q6
# list=[x**2 for x in range(0,10)]
# print(list)

# Q7
# mark=[]
# for i in range(6):
#     marks=int(input('enter marks='))
#     mark.append(marks)
# o=sum(mark)
# p=o/len(mark)
# mx=max(mark)
# mi=min(mark)
# print('total',o)
# print('percentile=',p)
# print('max',mx)
# print('min=',mi)
