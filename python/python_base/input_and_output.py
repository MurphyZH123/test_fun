


#输入姓名后输出欢迎语
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

# ########## 输出 ##########
# authorizing...
# Welcome to the matrix Mr. Jack.


#练习
name = input('your name is :')
gender = input('you are a girl?(y/n)')

welcome_str = 'Welcome to this site {prefix} {name}'
welcome_dic = {
	'prefix':'Mrs' if gender =='y' else 'Mr',
	'name':name
}

print('authorizing...')
print(welcome_str.format(**welcome_dic))

