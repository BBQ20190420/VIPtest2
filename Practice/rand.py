import random

#随机生成0到1的小数
print(random.random())
#随机生成2到10的浮点数
print(random.uniform(2,10))
#随机生成1到20的整数
print(random.randint(1,20))
#随机生成1到30之间间隔3的数，即1，4，7，3，13，16。。。。。
print(random.randrange(1,30,3))
ranlist=[2,6,123,"baby"]
ranstr="goodgirl"
#ranlist中，随机生成3个元素 ，可以是list，字符串，元组
print(random.choices(ranlist,k=3))
#ranstr中，随机生成单个元素
print(random.choice(ranstr))
#对ranlist随机排序
random.shuffle(ranlist)
print(ranlist)
#对fixlist随机排序，并取固定长度，但不改变原有顺序
fixlist=['adc','mm','job',3,6]
print(random.sample(fixlist,2))
print(fixlist)