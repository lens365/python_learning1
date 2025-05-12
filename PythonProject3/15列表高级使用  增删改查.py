"""
增   即添加
列表高级：  添加
1.append()追加   把数据添加在列表后面
2.insert   在指定位置插入元素、数据
3.extend()  通过extend()可以将列表追加到一个列表后面
"""
list=['铁锅炖大鹅','小鸡炖蘑菇']
print(list)
list.append('冻梨')
print(list)
list_1=['1','2','3']
print(list_1)
#insert()填入两个量，index，目标放在几号位置，object 填入的内容
list_1.insert(1,'4')
print(list_1)
num1=[1,2,3]
num2=[4,5,6]
#用法如下面所示，extend()包含的内容是添加在前面列表的后面
num1.extend(num2)
print(num1)
"""
改   即修改
将列表中的值进行修改，我们可以通过下标进行修改，注意列表第一个元素为0
"""
city_list=['beijing','shanghai','shenzhen','xian','wuhan']
print(city_list)
#将列表中的值进行修改
city_list[2]='guangzhou'
print(city_list)
#将列表中的值进行修改，我们可以通过下标进行修改，注意列表第一个元素为0

""""
找  即查找，查询
主要有in 和 not in
如果在，in将返回True，否则返回False
"""
food_list=['锅包肉','汆白肉','炒三丝']
food=input('请输入您想吃的食物')
if food not in food_list:
    print('不在')
else:
    print('在')
if food  in food_list:
    print('在')
else:
    print('不在')
#因此，in和not in互逆，我们日常开发主要用in
"""
删  即删除元素
常用的有：
1.del删除目标位置的数据
2.pop删除最后一个，并将删掉的数据缓存到列表名.pop()中
3，remove删除目标数据，比如我想删掉为w的数据
"""
a_list=['1','2','3','4','5','6','7','8','9']
print(a_list)
#del 应用场景为删除爬取数据中少量不想要的数据
del a_list[2]
print(a_list)
b=['1','2','3','4','5','6','7','8','9']
print(b)
#此时最后1个没了，删除列表中最后一个元素
b.pop()
print(b)
#此时下面的b.pop()代表着最后删掉的那个元素，把他缓存到栈里，因此打印时结果是如下结果
#而b.pop()还代表这种操作，因此上面操作是print(b)
print(b.pop())
c=['1','2','3','4','5','6','7','8','9']
print(c)
c.remove('3')
print(c)
#注意不能按下面这样操作,因为会返回none
#print(c.remove('3'))
###注意，实际上对于列表处理的各种方法而言，绝大多数都必须单独为一行，因为绝大多数都是返回  NONE，故不要和print()混用，实际上仅仅有pop()方法有返回值，其为开始删去的最后一个元素的缓存

