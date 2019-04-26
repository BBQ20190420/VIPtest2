#输出乘法口诀
# for i in range(1,10):
#     print()
#     for j in range(1,i+1):
#         print("%d*%d=%d"%(i,j,j*i),end=" ")

#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
# inithigh=100
# sum=100
# for i in range(1,11):
#     print(sum)
#     everhign=inithigh/(2**i)
#     print("第%d次的反弹高度是%f米"%(i,everhign))
#     sum=sum+everhign*2

#求1+2!+3!+...+20!的和
sum=0
n=1
for i in range(1,21):
    n*=i
    sum=sum+n
print(sum)
