import random

#冒泡法
def maopao():
    list=[]
    for i in range(3,15,2):
        list.append(i)
    print(list)
    #对list打乱顺序
    random.shuffle(list)
    print(list)
    for i in range(len(list)-1):
        for j in range(i):
            if list[j]>list[i]:
                list[i],list[j]=list[j],list[i]
        return list
#二分法
def erfen(number):
    list1 = []
    for i in range(4, 20, 3):
        list1.append(i)
    print(list1)
    random.shuffle(list1)
    print(list1)
    #number = int(input("请输入你想知道的值："))
    min = 0
    max = len(list1) - 1
    while min <= max:
        mid = ((min + max) // 2)
        if number == list1[mid]:
            return mid
        elif number > list1[mid]:
            min = mid + 1
        elif number<list[mid]:
            max=mid-1
index=erfen(4)
print(index)