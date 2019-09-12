#1
#COUNT = 0
#def Number(N):
#    global COUNT
#    for i in range(1,N):
#        fivenmuber=i*(3*i-1)/2
#        COUNT+=1
#       # print(fivenmuber)
#        if COUNT%10!=0:
#            print(fivenmuber,end="\t")
#           
#        else:
#            print(fivenmuber)
#Number(101)
#
#2
#def sum(n):
#    a=n%10
#    b=n//10/10
#    c=n//10%10
#    he=a+b+c
#    print('输出所有整数的和%d'%he)
#sum(234)

#3
#def three(a,b,c):
#    
#    area=[a,b,c]
#    area.sort()
#    print(area)
#
#a,b,c = map(float,input('输入数字').split())
#three(a,b,c)
#5
#COUNT=0
#def prin():
#    global COUNT
#    for i in range(49,91):
#        COUNT+=1
#        if COUNT%10!=0:
#            print(chr(i),end="\t")
#        else:
#            print(chr(i))
#prin()#

#def day(n):
#    for i in range(2010,n):
#        if i%4==0:
#            print('%d年今年有366天'%i)
#        else:
#            print('%d年今年有365天'%i)

#day(2021)
#7
##def distance(x1,x2,y1,y2):
#    dis = ((x2-x1)**2+(y2-y1)**2)**0.5
#    print('俩点间的距离:%f'%dis)
#distance(1,4,4,2)#




#8
from prettytable import PrettyTable
def mei(p):
    c = []
    b = []
    for p in range(2,32):
        if p>1:
            for i in range(2,p):
                if (p % i) == 0:
                    print(p,"不是质数")
                    break
                else:
                    print(p,"是质数")
                    d = 2**(p-1)
                    c.append([p,d])
    for x in c:
        if x not in b:
            b.append(x)
            table = PrettyTable(['p','2**(p-1)'])
    for row in b:
        table.add_row(row)
    print(table)
mei(5)








#9
#import time
#def main():
#    localtime = time.asctime(time.localtime(time.time()))
#   print("本地时间为 :", localtime)
#main()