# num=9
# score=90.5
# sex='girl'
# print(num,score,sex)
# print("number is %d"%num)
# #哒哒哒
# print("let's go")
"""
good boy!
"""
'''
good girl!
'''

# newnum=input("which number do you want to check:")
# print("you number is ",newnum)
#
# newscore=input("please tell me your score:")
# print("your score is",newscore)
#tom
# newname=input("please tell me your name:")bo
# print("your name is %s"%newname)

# name,age=input("请输入你的名字和年龄：").split(",")
# print("%s is %s"%(name,age))

# a=(3,8.9,'good')
# print(a.index('good'))
# print(a[0])
#
# list=[3,8.9,"good"]
# print(list[2])
# list.append(12)
# print(list)
#
#
# loglist=[]
# for i in range(0,30,2):
#     loglist.append(i)
#
# print(loglist)
#
# print(loglist[2:5])
# print(loglist[:-2:3])
# print(loglist[-8:-5])
# print(loglist[::6])
# print(loglist[:8:])
#
# print(loglist[2::5])
# #print(loglist.reverse())   #只实现效果
# loglist.reverse()
# print(loglist)

# badlist=[2,4,1,3,6,3]
# # badlist.sort()
# # print(badlist)
#
# # print(sorted(badlist))
# # print(badlist)
# badlist.insert(1,8)
# print(badlist)
# badlist.append('a')
# print(badlist)
# # badlist.extend(['good','bad'])
# # print(badlist)
# delete=badlist.pop(7)  #删除指定元素并返回该值
# print(delete)
# print(badlist)
# badlist.remove(1)
# print(badlist)
# print(badlist.count(3))
# print(max(badlist))
# print(min(badlist))
# print(len(badlist))
# del badlist[0]
# print(badlist)
# print(badlist.index(3))

# biglist=[]
# for i in range(1,10):
#     biglist.append(i)
# print(biglist)
# longtuple=tuple(biglist)
# print(longtuple)
# #longtuple.pop[0]
# print(type(longtuple))
# print(longtuple[-3])
# print(longtuple[3:8:2])

# pralist=[11,13,5,7,0,56,23,34,72]
# print("最大值是%d"%max(pralist))
# print("最小值是%d"%min(pralist))
# print("列表长度是%d"%len(pralist))
#
# print("56在列表中的位置是%d"%pralist.index(56))
# pralist.append(7)
# print("追加元素7后的列表是：",pralist)
# # del pralist[4]
# # # print("删除0后是%s"%pralist)
# pralist.pop(4)
# print("删除0后是:%s"%pralist)
#
# pralist.sort()
# pralist.reverse()
# #sorted(pralist)
# print("从大到小%s"%pralist)
# pralist.extend([66,67,68])
# print(pralist)

#集合
# s={9,3,5}
# print(s)
# s.add(8)
# print(s)
# s.remove(3)
# #s.remove(11)  #如果元素不存在，抛错
# print(s)
# s.discard(5)
# #s.discard(1) #如果元素不存在，不抛错
# print(s)
# s.clear()
# print(s)



firstdict={"lily":10,"tom":12,"mary":11,"bob":6}
print(firstdict)
print(type(firstdict))


print(firstdict['bob'])
firstdict['lily']=8
print(firstdict)
firstdict['fred']=20


print(firstdict)
print(firstdict.keys())
print(type(firstdict.keys()))

newlist1=list(firstdict)
print(newlist1)

print(firstdict.values())
print(firstdict.items())

for item in firstdict.items():
    print(item)

del firstdict['tom']
print(firstdict)

# firstdict.clear()
# print(firstdict)
