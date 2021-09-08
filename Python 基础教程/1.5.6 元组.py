# 元组属于不可变序列（元素集合），一旦创建，用任何方法都不可以修改其元素。
# 从形式上，元组的所有元素放在一对圆括号中，元素之间用逗号分隔。

# 元组与列表的区别
# 元组中的数据一旦定义就不允许更改。
#
# 元组没有append()、extend()和insert()等方法，无法向元组中添加元素。
#
# 元组没有remove()或pop()方法，也无法对元组元素进行del操作，不能从元组中删除元素。
#
# 从效果上看，tuple( )冻结列表，而list( )融化元组

# 元组的优点
# 元组的速度比列表更快。
#
# 元组对不需要改变的数据进行“写保护”将使得代码更加安全。
#
# 元组可用作字典键（特别是包含字符串、数值和其它元组这样的不可变数据的元组）。元组有时还作为函数的返回值返回（返回多个值）。
x = (1,2,3)

x =(3)
print(type(x))
x =(3,)
print(type(x))
# 使用tuple函数将其他序列转换为元组
print(tuple(range(5)))
print(tuple('abcdefg'))