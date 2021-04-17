"""
功能描述：
编写人：
编写日期：
实现逻辑：






"""

try:
    print(num)
except (IndexError,ImportError,NameError) as msg:
    print(msg)