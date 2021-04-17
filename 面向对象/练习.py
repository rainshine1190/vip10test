"""
功能描述：定义一个老师类，老师有姓名和性别，还有教的课程，可以教学，实现：xx老师，性别是xxx，教xxx课
编写人：
编写日期：
实现逻辑：

    类：Teacher

        属性：name,sex,course
        方法：teach

"""
#创建类
class Teacher():
    # 属性：name, sex, course
    def __init__(self,name,sex,course):
        self.name = name
        self.sex = sex
        self.course = course

    # 方法：teach
    def teach(self):
        print(f'{self.name}老师，性别是{self.sex}，教{self.course}课')


#创建对象
teacher1 = Teacher('liangchao','男','software testing')

teacher1.teach()