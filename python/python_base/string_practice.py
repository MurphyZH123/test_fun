"""
字符串基础
什么是字符串呢？字符串是由独立字符组成的一个序列，通常包含在单引号（''）双引号（""）或者三引号之中（''' '''或''''''，两者一样），比如下面几种写法。
"""

name = 'jason'
city = 'beijing'
text = "welcome to jike shijian"



#01,去掉开头和结尾都含有空字符，使用strip()函数

s = ' my name is jason '
new_s=s.strip()
#'my name is jason'
print(s)
print(new_s)


print('no data available for person with id: {}, name: {}'.format(id, name))


s = " ".join(map(str, range(0, 10)))
print(s)


name = input('your name:')
gender = input('you are a boy?(y/n)')

# ###### 输入 ######
# your name:Jack
# you are a boy?

welcome_str = 'Welcome to the matrix {prefix} {name}.'
welcome_dic = {
    'prefix': 'Mr.' if gender == 'y' else 'Mrs',
    'name': name
}

print('authorizing...')
print(welcome_str.format(**welcome_dic))

########## 输出 ##########
# authorizing...
# Welcome to the matrix Mr. Jack.



#03 split()函数
#split() 方法可以实现将一个字符串按照指定的分隔符切分成多个子串，
#这些子串会被保存到列表中（不包含分隔符），作为方法的返回值反馈回来。
"""
str.split(str="",num=string.count(str))[n]

参数说明：

str：（参数中的）表示为分隔符，默认为空格，但是不能为空('')。若字符串中没有分隔符，则把整个字符串作为列表的一个元素

num：表示分割次数。如果存在参数num，则仅分隔成 num+1 个子字符串，并且每一个子字符串可以赋给新的变量

[n]：表示选取第n个分片

"""

#例子01
u = "www.doiido.com.cn"
 
#使用默认分隔符
print(u.split())

 
#以"."为分隔符
print(u.split('.'))

 
#分割0次
print(u.split('.',0))

 
#分割一次
print(u.split('.',1))

 
#分割两次
print(u.split('.',2))

 
#分割两次，并取序列为1的项
print(u.split('.',2)[1])

 
#分割最多次（实际与不加num参数相同）
print(u.split('.',-1))
 
#分割两次，并把分割后的三个部分保存到三个文件
u1,u2,u3 = u.split('.',2)
print(u1)

print(u2)

print(u3)

 
#去掉换行符
c = '''say
hello
baby'''
 
print(c)

 
print(c.split('\n'))



#例子02
string="hello boy<[www.doiido.com]>byebye"
  
print(string.split("[")[1].split("]")[0])

  
print(string.split("[")[1].split("]")[0].split("."))











