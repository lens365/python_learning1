'''
对于数字而言，
int：有符号整型
long：长整型->对于py2
float：小数  注意 py里面没有double
对于布尔型而言：
有true   1
与false  0
对于字符串而言：
如：”这就是字符串“
对于列表：
还要元组，其与列表类似，其为表示多个数据的一个集合

'''
from operator import truediv

#int
money=5000
#float
money1=1.2
#bool
#流程控制语句
#性别->在企业开发就使用sex，gender
sex=True
#男->True
#女->False
#字符串string
string1="苍茫的天涯是我的爱"
#单引号双引号均可
string2="'嘿嘿嘿'"
print(string2)
#高级数据类型
#list列表  当获取到了很多数据，存储到列表中，等后面访问列表
name_list=["周杰伦","科比"]
print(name_list)
#tuple 元组   其不可再进行更改，这是list于其的区别，它是用圆括号（）
#dic字典   scrapy框架使用
#变量名是{key：value}
person={
    'name':"红浪漫",
    'age':18
}