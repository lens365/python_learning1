#for循环语句
#range（）如何用
#一个一个输出叫做遍历，也叫做循环
#格式： for 变量名 in 要遍历的数据
s=('china')
print(s)
#i代表的是变量名，s代表要遍历的数据
for i in s:
    print(i)
#range()的使用:range从0开始，为左闭右开区间
for j in range(1,6):
    print(j)
#range()除此之外，还可以增加一个参数，另一参数为步长，即再加一个步长到下一个
for j in range(1,6,2):
    print(j)
#应用场景：爬取一个列表来返回
#循环一个列表
a_list=['周杰伦','林俊杰','林志炫']
for i in range(1,3,2):
    print(a_list[i])
print(len(a_list))
for i in range(0,len(a_list)):
    print(a_list[i])
