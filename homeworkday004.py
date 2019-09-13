#1
#def score():
#    a,b,c,d=map(int,input('请输入成绩').split())
#    list2=[a,b,c,d]
#    list1=sorted(list2)
#    num=list1[-1]
#    print(num)
#    he=[a,b,c,d]
#    for i in  he:
#        
#        if i>=num-10 :
#            print('A')
#        elif i>=num-20 :
#                print('B')
#        elif i>=num-30 :
#                print('C')
#        elif i>=num-40 :
#                    print('D')
#        else:
#                        print('F')
#    
#
#
#
#score()

#2

#def number():
#    a=[1,2,3,1,3,4,5,'h','w','h']
#    print(a)
#    print(a[::-1])
#
#number()

#3

#
#def numb():
#    a,b,c,d,e,f,g,l,k=map(int,input('Enter inters between 1 and 100: ').split())
#    number=[a,b,c,d,e,f,g,l,k]
#    number1=[]
#    for i in number:
#        if i not in number1:
#            number1.append(i)
#    print(number1)
#    for  i in range(len(number1)):
#        num11=0
#        for j in range(len(number)):
#            if number[j]==number1[i]:
#                    num11+=1
#                    
#            else:
#                    num11=num11
#        print('有这么多个一样的数%d'%num11)
#        
#numb()
##4
#def socre():
#    a,b,c,d,f=map(int,input('请输入成绩').split())
#    aver=(a+b+c+d+f)/5
#    he=[a,b,c,d,f]
#    for i in he:
#        if i>aver:
#            print('大于平均分的分数有 :%d'%i)
#        elif i==aver:
#            print('等于平均分的分数有 :%d'%i)
#        else:
#            print('小于平均分的分数有 :%d'%i)
#socre()

#5

#6 
a,b,c,d=map(int,input('几个数').split())
list2=[a,b,c,d]
list1=sorted(list2)
print(list1)
for i in range(4):
    if list1[0]==list2[i]:
        print(i)
    else:
        pass
