"""
功能描述：
编写人：
编写日期：
实现逻辑：






"""

try:
    print(1)
except Exception as result:
    print('有错误')
else:
    print('没错误的时候我就会被执行')
finally:
    print('没异常也好，有异常也罢，我都会被执行')