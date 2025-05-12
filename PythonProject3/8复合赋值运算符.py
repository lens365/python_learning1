a=1
print(a)
#这一语句本质上等于a=a+2
a+=2
print(a)
b=1
print(b)
#这一语句与b=b*3 本质相同
b*=3
print(b)
c=1
print(c)
#本质与c=c-2相同
c-=2
print(c)
d=1
print(d)
#本质与d=d/2相同
d/=2
print(d)
#因此+=  -=  *=  /=本质都是对其本身的操作，这就是复合赋值运算符
#下面继续
#整除的运算不要搞错，是除法得到的结果保留整数部分（向下取整数）  如：5//2=2  -5//2=-3
e=2
print(e)
e//=3
print(e)
f=3
print(f)
f%=2
print(f)
g=2
g**=2
print(g)
#因此我们可以看出，我们学习的算术运算符，均可通过复合赋值运算符来灵活·运用
