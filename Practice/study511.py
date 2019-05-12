#import study
import re
# def cal(*nums):
#     sum=0
#     print(*nums)  #打印出来的是一个一个元素，没有类型，打印type（*nums）会报错
#     print(nums) #打印出来的是一个元组
#     print(type(nums))
#     for n in nums:
#         print(type(n))
#         sum=sum+int(n)
#     return sum
#
# #print(cal(1,2,3,'4'))
# list=[1,6,9,'7']
# tup=(1,5,6)
#想要调用，必须加*
#print(cal(*list))
#print(cal(*tup))


# def person(name,*age,**kwargs):
#     print(name,age,kwargs)
# person("bob")
# person("may",6)
# person('ab',sex='female',gm='65')
# person('mob',5,'good')
# person('mob',(5,'good'))
# food={'fruit':'apple','age':1}
# person("jjd",**food)
# #person('mom',sex=2,55)  关键字必须在位置参数等之后
# def allcal(x,y,symbol):
#     if symbol == '加' or symbol == '+':
#         result = int(x) + int(y)
#     elif symbol == '减' or symbol == '-':
#         result = int(x) - int(y)
#     elif symbol == '乘' or symbol == '*':
#         result = int(x) * int(y)
#     elif symbol == '除' or symbol == '/':
#         result = int(x) / int(y)
#     else:
#         print("您输入等符号有误，无法计算")
#     return result
#
#
# m, n, s = input("输入两个数字和您想要的计算方式").split(",")
# myresult = (allcal(m, n, s))
# print("%s%s%s=%d" % (m, s, n, myresult))

# print("gloabl")
# print(__name__)



# if __name__ == '__main__':
#     m, n, s = input("输入两个数字和您想要的计算方式").split(",")
#     myresult = (allcal(m, n, s))
#     print("%s%s%s=%d" % (m, s, n, myresult))


# def cal(a,b):
#
#     try:
#         print(a/b)
#     except :
#         print('nonameerror')
#     # except ZeroDivisionError as error:
#     #     print(error)
#     #     print("myerror")
#     # except BaseException as dd:
#     #     print(dd)
#     else:
#         print('jdhh')
#     finally:
#         print("all")
#
#
# cal(2,0)

# mytxt=open("/Users/bqq/PycharmProjects/qqtest/VIPtest2/Practice/data.txt",'r')
# print(mytxt)
# # for i in mytxt:
# #     print(i)
# # print(mytxt.read())
# # print(mytxt.read(2))#行
# #print(mytxt.readline())
# #print(mytxt.readlines())
# for i in mytxt.readlines():
#     print(i)
# print(mytxt.tell())
#mytxt.close()

# wtxt=open('/Users/bqq/PycharmProjects/qqtest/VIPtest2/Practice/data1.txt','r+')
# # wtxt.write("白白胖胖")
# # print(wtxt.readlines())
# # wtxt.close()

# datatxt=open('/Users/bqq/PycharmProjects/qqtest/VIPtest2/Practice/data1.txt','r+')
# # newstr=[]
# #
# # lines=datatxt.readlines()
# # # for i in lines:
# # #     # print(type(i))
# # #     # print(i)
# # #     n =re.findall("\d+", i)
# # #     # print(n)
# # #     # print(type(n))
# # #     for j in n:
# # #         # if j :
# # #         newstr.append(j)
# # for i in lines:
# #     for j in i:
# #         if j.isdigit():
# #             print(j)
# #             newstr.append(j)
# #
# # print(newstr)
# # newlist1=[]
# # for x in newstr:
# #     newlist1.append(int(x))
# # print(newlist1.sort())
# # print(newlist1)
# # with open("/Users/bqq/PycharmProjects/qqtest/VIPtest2/Practice/data2.txt", 'w+') as f:
# #     #f.writelines(newstr)
# #      for y in newlist1:
# #          f.write(str(y))
# # datatxt.close()

# class Student():
#     def __init__(self,sno):
#         self.mysno=sno
#         #print(sno)
#     def study(self,course):
#         #print("学号%s的学生,学习了%s课程"%(self.sno1,course))
#         return course
# # wow=Student("123")
# #wow.study("math")
#
#
# class Teacher(Student):
#     def __init__(self,gh,no):
#         self.gh=gh
#         self.mysno=no
#         #self.sno=sno
#         self.subject=self.study('math')
#     #subject=Student('234').study('math')
#     #subject=Student('234').study('math')
#
#
#     def tech(self, teacher,place,money):
#         print("工号为%s的%s教%s课程" % ( self.gh,teacher, self.subject))
#         print("%s在%s工作"%(teacher,place))
#         print("%s的工资是%d"%(teacher,money))
#         print("%s学号"%(self.mysno))
#
#
# Teacher('9999').tech("小明老师",'beijing',20000)

class Base():
    def test(self):
        print("this is test!")

class A(Base):
    def test(self):
        print("this is testA")

class B(Base):
    def test(self):
        print("this is testB")
class C(A,B):
    def test(self):
        print("this is testC")

cc=C()
cc.test()
