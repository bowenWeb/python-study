## 基础
定义变量
索引
切片
isinstance 和 type 的区别在于：
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
eval 去除字符串引号，有脚本植入风险
操作运算符
|操作符 |描述|
|<	   |小于|
|<=    |小于或等于|
|>     |大于|
|>=    |大于或等于|
|==    |等于，比较两个值是否相等|
|!=    |不等于|

逻辑运算符
and 
or
not

## 数据类型
### Number（数字）
- int 10
- float 15.20
- complex（复数）3.14j

### String（字符串）
Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符

### bool（布尔类型）
布尔类型只有两个值：True 和 False

### List（列表）
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]  # 定义一个列表

### Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。元组中的元素类型也可以不相同：
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

输出结果：
('abcd', 786, 2.23, 'runoob', 70.2)
abcd
(786, 2.23)
(2.23, 'runoob', 70.2)
(123, 'runoob', 123, 'runoob')
('abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob')

### Set（集合）
在 Python 中，集合使用大括号 {} 表示，元素之间用逗号 , 分隔。另外，也可以使用 set() 函数创建集合。


### Dictionary（字典）
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。键(key)必须使用不可变类型。在同一个字典中，键(key)必须是唯一的。

### bytes 类型
bytes 类型表示的是不可变的二进制序列，创建 bytes 对象的方式有多种，最常见的方式是使用 b 前缀：此外，也可以使用 bytes() 函数将其他类型的对象转换为 bytes 类型。bytes() 函数的第一个参数是要转换的对象，第二个参数是编码方式，如果省略第二个参数，则默认使用 UTF-8 编码：
x = bytes("hello", encoding="utf-8")


## 流程控制
### if 语句
```
#!/usr/bin/python3
 
var1 = 100
if var1:
    print ("1 - if 表达式条件为 true")
    print (var1)
 
var2 = 0
if var2:
    print ("2 - if 表达式条件为 true")
    print (var2)
print ("Good bye!")

```
### 三元表达式
格式：条件成立的结果 if 条件 else 条件不成立的结果
```
score = 88
print('及格') if score >= 60 else print('不及格')
```

### while 循环
break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。

continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。

```
#!/usr/bin/python3
 
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")

```

```
for x in range(6):
  print(x)
else:
  print("Finally finished!")

```

## 函数
```
def 函数名（参数列表）:
    函数体

```

```
#!/usr/bin/python3
 
def max(a, b):
    if a > b:
        return a
    else:
        return b
 
a = 4
b = 5
print(max(a, b))
```

### 默认参数
```
#!/usr/bin/python3
 
#可写函数说明
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="runoob" )
print ("------------------------")
printinfo( name="runoob" )

```

### 不定长参数
```
#!/usr/bin/python3
  
# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
 
# 调用printinfo 函数
printinfo( 70, 60, 50 )

```

### 关键字可变参数
```
#!/usr/bin/python3
  
# 可写函数说明
def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
 
# 调用printinfo 函数
printinfo(1, a=2,b=3)
```


## 错误和异常

```
while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")
```