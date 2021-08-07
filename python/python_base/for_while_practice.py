"""
当我们同时需要索引和元素时，还有一种更简洁的方式，那就是通过 Python 内置的函数 enumerate()。
该函数适用于list、dict
"""

#01，针对于list
l = [1, 2, 3, 4, 5, 6, 7]
for index, item in enumerate(l):
    if index < 2:
        print(item)  


#02，针对于dict
dict1 ={'name':'Murphy','gender':'famale','age':'2'}
for k,v in enumerate(dict1):
	print(f'索引index是{k},值value是{v}')



l = [1, 2, 3, 4]
index = 0
while index < len(l):
    print(l[index])
    index += 1




text = ' Today,  is, Sunday'
text_list = [s.strip() for s in text.split(',') if len(s.strip()) > 3]
print(text_list)
['Today', 'Sunday']

l=[]
text2 ='  Today,  is, Sunday'
for i in text2.split(','):
	if len(i.strip())>1:
		l.append(i.strip())
print(l)

attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'], ['mike', '1999-01-01', 'male'],['nancy', '2001-02-01', 'female']]
text_dict = [dict(zip(attributes,value)) for value in values]
print(text_dict)


l = []
for value in values:
    d = {}
    for i in range(3):
        d[attributes[i]] = value[i]
    l.append(d)









