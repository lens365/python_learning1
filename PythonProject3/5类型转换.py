#转换为整形
#str->int
a='123'
print(int(a))
print(type(int(a)))
#float->int
a=1.23
print(int(a))
#此时，打印的结果会舍去后面的值，因为他不会存储进后面，他并不会四舍五入
#bool->int
b=True
print(int(b))
#False->0  True->1
#当字符串里面有特殊字符是不可转换的，非法字符会报错的
#比如a="1.23"  print(int(a))会报错
#转换为浮点数   当我们在爬虫时，大部分获取的都是字符串类型，我们就对其进行一个类型转换
#字符串->浮点数
a="1.23"
print(float(a))
#整形转换为浮点数
a=66
print(float(a))
#转成字符串
#大部分应用场景：整型转成字符串
a=80
print(str(a))
print(type(str(a)))
#注意注意，一定是str  不是string
b=80.1112
print(str(b))
print(type(str(b)))
#布尔型转换为字符串,会以True，False存储，而不是数字
a=True
print(str(a))
print(type(str(a)))
#转换为布尔类型，对于非零的转换，那么全是True
a=2
print(bool(a))
print(type(bool(a)))
#浮点数转换为布尔类型
a=-1.0
print(bool(a))
print(type(bool(a)))
#只要是非零均为True
#字符串转换为布尔值
a="111建材"
print(bool(a))
print(type(bool(a)))
#这里面只要有内容，就是True,哪怕里面是空格
#列表转换成布尔值，类似的，只要里面有内容，就是True
#元组在此与列表类似，若为空，即为False
a=( )
print(bool(a))
#同理，dic也是如此，里面有东西即为True
a={'name':'周杰伦'}
print(bool(a))
print(type(bool(a)))
