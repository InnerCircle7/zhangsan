# 判断 由 缩进 代表 代码块
# a = 1
# b = 2
# if a == 1:
#     print("哈哈哈")

# if a > b:
#     print("a比b大")
# else：
#     print("b更大")

# age = int(input("请输入你的年龄："))
# if age > 60:
#     print("您应该退休了")
# elif age > 30:
#     print("家庭的责任很重吧")
# elif age > 20:
#     print("一定要好好规划你的未来!")
# else:
#     print("读书的时候 要认真！")

# if age > 20 and age <= 30:  # 多条件同时满足
#     print("22222222")  

# 判断条件 ==,!=,>,<,in,is,not in,not is 

# a = "你好"
# if a in "你好，今天你吃了吗？":
#     print("OK")
# else:
#     print("不OK")

# a = input("请输入：")
# if a == "":
#     print("不能为空！")
#     exit()

# if a in "0123456789":
#     a = int(a)
# else:
#     print("请输入正确的年龄！")
#     exit()

# if a > 5:
#     print("大")
# else:
#     print("小")

# a = "aaa"
# if type(a) is int:
#     print("是数字！")
# elif type(a) is str:
#     print("是字符串")
# else:
#     print("其他")

# 循环 while for
# a = 1
# while a < 10:
#     print("哈哈哈",a)
#     a = a + 2

"""
练习：现在有10个学生的成绩，需要录入到系统中，
这10个人分别是：张三、李四、王麻子、浪晋、流云、希希、小梁、二狗、陈平安、朱珠
并且名字和成绩需要对应上 而已大于60和小于60的要分开存放
"""
high = {}
low = {}
studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠"]
a = 0
while a < len(studentlist):
    chengji = int(input("请输入"+studentlist[a]+"的成绩："))
    if chengji >= 60:
        high[studentlist[a]] = chengji
    else:
        low[studentlist[a]] = chengji
    a = a + 1
print("大于60的：",high)
print("小于60的：",low)
