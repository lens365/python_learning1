#对于爬取的数据的处理
#下面是常用的方法
'''
1.len 判断长度，判断字符串长度，也可以判断列表长度
2.find 内容查找 ，查找内容是否在字符串中存在，如果存在，那么返回第一次出现的地方的索引位置，如果不存在，则返回-1
注意字符串第一个同列表是类似的，都是0开始
3.判断语句 startswith,endswith:判断是否以什么开头或以什么结尾
4.count 统计某些字符出现次数
5.replace 替换字符串里面的东西，若用count指定了次数，则它不会超过count次
6.split 切割掉想去掉的地方
7.upper,lower 转大写和转小写
8.strip 去空格
9.join 拼接
'''
s='china'
print(len(s))
print(s.find('h'))
print(s.find('n'))
print(s.find('b'))
#startswith方法用于判断开头的是否为目标值，若是：True，不是则为False
print(s.startswith('c'))
print(s.endswith('d'))
#count()方法使用
print(s.count('n'))
s2='aaabbba#'
print(s2.count('a'))
#如下面所示，前面的是要替换的部分，后面是想换成的内容
print(s2.replace('b','c'))
print(s2.split('#'))
#当什么都不传时，把所有字母都变成大写
s3=s2.upper()
print(s2.upper())
print(s3.lower())
s4='     a      '
print(s4.strip())
s5=('a')
#这里表示了join较为复杂，我们先不管
print(s5.join('hello'))

