#逻辑运算符 not非  and与  or或
#and 只有两边都是True的时候才会返回True
print(10>20 and 10<20)
print(10<11 and 10<20)
#or 只要有一边是True，就是True
print(10>20 or 10>15)
print(10>30 or 10<20)
#not 取反 如果是True,那么结果为False
print(not True)
print(not 10>20)
#逻辑运算符性能的提升
#and的性能优化
a=35
a>10 and print("hello world")
a<10 and print("hello world")
#因为and 是只有均为True才成立的，因此，前面为True，后面也会按True来执行，而前面是False，后面就会按照False来执行，因为没有意义继续下去了


#or的性能优化
a=38
a>39 or print("hello world")
a<39 or print("hello world")
#or只要有一个为True，结果就是True，所以不用管后面的部分
