#普通输出
print("故事里的小黄花，从出生那年一直在那飘着")
#格式化输出
print('我年龄为'+str(18))
name='周杰伦'
age=18
#  %s加字符串，%d是数值
print("我的名字是%s,我的年龄是%d"%(name,age))
#上面的是比较传统的%输入方式，下面我们有f-string法
print(f"我的名字是{name},我的年龄是{age}")
#明显的，下面这种更加简单易懂 ，建议多使用f-string
#输入  input()函数
password=input("请输入银行卡密码")
print(f'密码为{password}')