import time #控制时间的包 编程习惯写到最上面
import random #生成随机数
import pymysql

pymysql.connect(host="127.0.0.1",user="root",password="123456",db="testdb")
cur = db.cursor()
try:
    cur.execute("select * from t_class;")
    res = cur.fetchall()
    print(res)
except:
    print("sql语句有误")

# a = input("请输入你的名字：")
# b = input("请输入你的年龄：")
# try:
#     if int(b) > 18:
#         print(a,"成年了")
#     else:
#         print(a,"未成年")
# except:
#     print("请输入正确的年龄")

# 处理用户输入的数据
# 代码的单位 包->模块->类->方法->变量 既包含又并列
# 包->系统自带的 第三方的 
# pip->管理第三方包的工具 pip install 包名 安装 pip uninstall 包名 pip/pip3 list 查看已安装的第三方包
# 常用的第三方的包 pymysql-数据库 Selenium-web自动化 appium-app自动化
#  request 接口自动化 xlrd 操作excel表 xlwt 读取excel表 ...

# for i in range(10):
#     time.sleep(1)
#     print(i)

# a = random.randint(100,1000)
# print(a)
# 模块->包下面的.py文件

"""
练习：
定义一个方法，用来判断用户输入的账号密码是否符合规范。
"""
# def check(username,password):
#     """
#     自动的判断账号长度是5-8位，密码长度6-12位，并且账号必须是小写开头
#     """
#     if len(username) >= 5 and len(username) <= 8:
#         if username[0] in "qazwsxedcrfvtgbyhnujmikolp":
#             if len(password) >= 6 and len(password) <= 12:
#                 return True
#             else:
#                 return "密码长度必须是6-12位"
#         else:
#             return "账号必须小写字母开头"
#     else:
#         return "账号长度必须是5-8位"

# print(check("a1234","1223111"))