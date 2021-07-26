####实例001:数字组合
"""
题目：**题目：**有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

**程序分析：**遍历全部可能，把有重复的剃掉。
"""
# total=0
# for i in range(1,5):
# 	for j in range(1,5):
# 		for k in range(1,5):
# 			if ((i!=j)and(i!=k)and(j!=k)):
# 				print(i,j,k)
# 				total+=1
# print(total)






#### 实例002：“个税计算”
"""
**题目：**企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？

**程序分析：**分区间计算即可。
"""
# profit_input=int(input('请输入当月的利润:'))
# profit=profit_input
# bonus=0
# thresholds=[100000,100000,200000,200000,400000]
# rates=[0.1,0.075,0.05,0.03,0.015,0.01]
# for i in range(len(thresholds)):
# 	if profit<=thresholds[i]:
# 		bonus=bonus+profit*rates[i]
# 		profit=0
# 		break
# 	else:
# 		bonus=bonus+thresholds[i]*rates[i]
# 		profit=profit-thresholds[i]
# bonus=bonus+profit*rates[-1]
# print(f'当前月的利润为:{profit_input},应发放的奖金为{bonus}')

profit_input=int(input('请输入当月的利润:'))
profit=profit_input
bonus=0
thresholds=[100000,100000,200000,200000,400000]
rates=[0.1,0.075,0.05,0.03,0.015,0.01]
for i in range(len(thresholds)):
	if profit <= thresholds[i]:
		bonus = bonus+profit*rates[i]
		profit = 0
		break
	else:
		bonus = bonus+thresholds[i]*rates[i]
		profit = profit - thresholds[i]
bonus = bonus+profit*rates[-1]
print(f'当前月的利润为:{profit_input},应发放的奖金为{bonus}')

####实例003:完全平方数

"""
**题目：**一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

**程序分析：**因为168对于指数爆炸来说实在太小了，所以可以直接省略数学分析，用最朴素的方法来获取上限:
"""
# n=0
# while (n+1)**2-n**n<=168:
# 	n=n+1
# for i in range((n+1)**2):
# 	if i**0.5==int(i**0.5)and(i+168)**0.5==int((i+168)**0.5):
# 		print(i-100)





####实例004:今天是今年的第几天
"""
**题目:**输入某年某月某日，判断这一天的是这一年的第几天？

"""
def isLeapYear(y):
	return (y%400==0 or (y%4==0 and y%100!=0))

DoFM=[0,31,28,31,30,31,30,31,31,30,31,30]
res=0
year=int(input('请输入几年的年份'))
month=int(input('请输入几年的月份'))
day=int(input('请输入当前天数'))
if isLeapYear(year):
	DoFM[2]=DoFM[2]+1
for i in range(month):
	res=res+DoFM[i]
print(f'当前年份{year},当前月份{month},当前天数{day},当前日期是今年的第{res+day}天')











