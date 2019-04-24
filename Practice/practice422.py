import ddt


# def Word(word, retry=3, words="please try again!"):
#     while True:
#         newword = input(word)
#         if newword in ('y', 'yes', "YES"):
#             return True
#         if newword in ('n', 'no', "NO"):
#             return False
#         retry = retry - 1
#         if retry < 0:
#             raise OSError("error")
#         print(words)
#
# Word('j')

# def fix(num,name="lily",age=3):
#     print(num)
#     print(name)
#     print(age)
# #正确调用函数方法，name，age是可变参数（可传可不传），num是必传
# fix(8)
#
# fix(8,name="tom")
#
# fix(8,name='bob',age=9)
# #错误调用方式
# fix(name="hero")


#可变参数,*arg后面的参数，只能是关键参数
# def changePar(*args):
#     print(args)
# changePar(1,4,'k')
#
# def changeDicPar(**kwargs):
#     print(kwargs)
# changeDicPar(a=2,b='q',c=8,d='g')
#
# def concat(*args,spl="/"):
#     return spl.join(args)
#
# print(concat("mom",'dad','son'))

list=[range(3,6)]
print(list)
# arg=[3,6]
# print(list(range(*arg)))