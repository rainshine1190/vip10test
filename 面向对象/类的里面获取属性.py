"""
功能描述：
编写人：
编写日期：
实现逻辑：






"""

class Washer():
    #属性
    #方法
    def wash(self):
        print(f'hair1的洗衣机宽度是{self.width}')
        print(f'hair1的洗衣机高度是{self.height}')
        print(self)
        # print(f'{self.weight}')



# hair2 = Washer()
hair1 = Washer()
#
# hair2.weight = 100
# hair2.wash()
# print(hair2)


hair1.width = 500
hair1.height = 800
hair1.wash()
print(hair1)