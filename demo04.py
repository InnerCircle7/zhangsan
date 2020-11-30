"""
class 声明类的名字
然后类的名字的首字母必须大写
面向对象编程
类里面所有的方法，都必须要传一个参数，叫self
"""

class Girlfriend():
    def __init__(self):
        """
        女朋友 属性
        """
        self.sex = "女"
        self.high = "162cm"
        self.weigh = "52kg"
        self.hair = "大波浪"
        self.age = "18岁"
    
    def caiyi(self,num):
        """
        才艺表演
        """
        if num == 1:
            print("胸口碎大石！")
        elif num == 2:
            peint("唱、跳、rap、篮球")
        else:
            print("单手开瓶盖")
    
    def chuyi(self):
        """
        厨艺持家
        """
        print("精通八大菜系！啥都会！")

    def work(self):
        """
        工作挣钱
        """
        print("开挖掘机！")