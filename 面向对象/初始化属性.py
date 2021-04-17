"""
功能描述：
编写人：
编写日期：
实现逻辑：






"""

# class Washer():
#     #属性
#     def __init__(self):
#         print('我被执行了')
#         self.width = 500
#         self.height = 800
#         self.brand = '海尔'
#
#     #方法
#     def wash(self):
#         print(f'hair1的洗衣机宽度是{self.width}')
#         print(f'hair1的洗衣机高度是{self.height}')
#
# hair2 = Washer()
# hair1 = Washer()
# a = Washer()
#
# hair1.wash()


class Washer():
    #属性
    def __init__(self,width,height,brand):
        print('我被执行了')
        self.width = width
        self.height = height
        self.brand = brand

    #方法
    def print_info(self):
        print(f'hair1的洗衣机宽度是{self.width}')
        print(f'hair1的洗衣机高度是{self.height}')
        print(f'hair1的洗衣机品牌是{self.brand}')

    def __str__(self):
        return f'这是{self.brand}洗⾐衣机的说明书'

    def __del__(self):
        print('我被删除了')

hair1 = Washer(100,200,'西门子')
hair2 = Washer(100,200,'西门子')
# hair1 = Washer()
print(hair2)

hair2.print_info()

