count=3
while count>0:
    user, password = input("请输入用户名和密码,以逗号隔开:").split(",")
    if user=="admin" and password=="123456":
        print("登录成功")
    else:
        print("用户名或错误！")
        count-=1