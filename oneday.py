#temperature=float(input('请输入一个华氏温度'))
#temp2=((temperature-32)/1.8)
#print('转化的温度是%f'%temp2)

#number=(input('请输入一个数'))
#bai=int(number[0])
##shi=int(number[1])
#ge=int(number[2])
#if bai ** 3 + shi **3 + ge **3 == int(number) :
#            print('是水仙花数')
#else:
  #          print('不是水仙花数')

1

#celsius=float(input('Enter a degree in celsius '))
#fahrenheit = (9/5)*celsius + 32
#print('43 celsius is %.1f Fahrenheit'%fahrenheit)

2 
#import math
#math.pi
#radius,length = map(float,input('Enter the radius and length of a cylinder : ').split())
#area =( radius * radius * math.pi)
#volume= (area * length)
#print('The area is %.4f'%area)
#print('The volume is %.1f'%volume)

3
#Value=float(input('Enter a value for feet :'))
#meter=Value * 0.305
#print('%.1f feet is %.4f meters'%(Value,meter))

4
#kilograms=float(input('Enter the amount of water in kilograms :'))
#initialTemperature=float(input('Enter the initial temperature :'))
#finalTemprature=float(input('Enter the final temperature :'))
#Q=kilograms*(finalTemprature - initialTemperature) * 4184
#print('The energy needed is %.1f'%Q)
5

#balanch,rate=map(float,input('Enter blance and interest rate(e.g., 3 for 3%)').split())
#interest=balanch*(rate/1200)
#print('The interest is %.5f'%interest)

6
#v0,v1,t=map(float,input('Enter vo, v1, and t:').split())
#a=(v1-v0)/t
#print('The average acceleration is %.4f'%a)
7

#a=float(input('Enter the monthly saving amount :'))
#one=a*(1+0.00417)
#two=(a+one)*(1+0.00417)
#see=(a+two)*(1+0.00417)
#four=(a+see)*(1+0.00417)
#five=(a+four)*(1+0.00417)
#Six=(a+five)*(1+0.00417)
#print('After the sixth month , the account value is %.2f'%Six)

8
number=int(input('Enter a number between 0 and 1000 :'))
a=number/100
b=number//10%10
c=number%10
sum=a+b+c
print('The sum of the digits is %d'%sum)