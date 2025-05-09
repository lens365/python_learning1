#if语句
#if要判断的条件：
#   条件成立时要做的事情
age=19
if age >18:
    print("你可以开车")
gender=True
if gender:
    print("男性")
else:
    print("女性")
#对于if而言，当条件为True，则会运行，而男性为True，女性为False
age=int(input("请输入年龄"))
#input输入的默认是字符串，而字符串是不能与数字进行比较，因此要强制类型转换
if age>= 18:
    print("你可以去网吧")
else:
    print("未成年不允许进网吧")
#ifelse语法
#if是满足条件，为True时执行，而当是False不执行
#当有else，则需要执行else中的内容


#elif
#以下为案例
a=85
if a>=90:
    print("恭喜获得优秀")
elif a>=80:
    print("你的成绩为良好")
elif a>=70:
    print("成绩为中")
else:
    print("你不合格")