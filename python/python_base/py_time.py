#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '操作时间的工具类'

"""
import datetime
import time


# ==========================
# ========== time ==========
# ==========================


def getCurrentMilliSecondTime():
   """
    description:  获取当前时间-毫秒级
     return:       1557730376981 -> str
   """
    timestamps = str(round(time.time() * 1000))
    return timestamps


def getCurrentSecondTime():
    """
    description:  获取当前时间-秒级
    return:       1557730377 -> str
 29     """
 30     timestamps = str(round(time.time()))
 31     return timestamps
 32
 33
 34 def getCurrentTimeTuple(times=time.time()):
 35     """
 36     description:  接受秒级时间戳并返回时间元组（与mktime(tuple)相反）
 37     times:        默认当前时间 可传second
 38     return:       (tm_year=2019, tm_mon=5, tm_mday=13, tm_hour=10, tm_min=9, tm_sec=18, tm_wday=0, tm_yday=133, tm_isdst=0) -> tuple
 39     tips:         time.localtime() 不传参则取当前时间
 40     """
 41     timestamps = time.localtime(times)
 42     return timestamps
 43
 44
 45 def getTimeByTuple(tupleTime=time.localtime()):
 46     """
 47     description:  接受时间元组并返回秒级时间戳（与localtime(sec)相反）
 48     tupleTime:    默认当前时间的元组 可通过time.localtime() or datetime.datetime.now().timetuple()获取
 49     return:       1557733061 -> str
 50     """
 51     timestamps = str(round(time.mktime(tupleTime)))
 52     return timestamps
 53
 54
 55 def getCurrentFormatTimeStr(times=time.time()):
 56     """
 57     description:  将指定时间元组格式化为字符串
 58     times:        默认当前时间 可传second
 59     return:       2019-05-13 15:00:47 -> str
 60     tips:         %y 两位数的年份表示（00-99）    %Y 四位数的年份表示（000-9999）   %m 月份（01-12）    %d 月内中的一天（0-31）
 61                   %H 24小时制小时数（0-23）      %I 12小时制小时数（01-12）        %M 分钟数（00=59）  %S 秒（00-59）   %w 星期（0-6）
 62     """
 63     timestamps = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(times))
 64     return timestamps
 65
 66
 67 def getCurrentTimeTupleByFormatStr(time_str=str(datetime.datetime.now()).split(".")[0], format_type="%Y-%m-%d %H:%M:%S"):
 68     """
 69     description:  接受格式化字符串返回时间元组
 70     time_str:     格式化字符串   如:2019-05-13 15:00:47    默认当前时间
 71     format_type:  格式化规则    如:%Y-%m-%d %H:%M:%S      默认%Y-%m-%d %H:%M:%S
 72     return:       (tm_year=2019, tm_mon=5, tm_mday=13, tm_hour=10, tm_min=9, tm_sec=18, tm_wday=0, tm_yday=133, tm_isdst=0) -> tuple
 73     """
 74     return time.strptime(time_str, format_type)
 75
 76
 77 def getCurrentTimeStr():
 78     """
 79     description:  获取当前时间的可读形式字符串
 80     return:       Mon May 13 11:27:42 2019 -> str
 81     """
 82     return time.ctime()
 83
 84
 85 def getCurrentTimeStrByTuple(tupleTime=time.localtime()):
 86     """
 87     description:  获取指定时间的可读形式字符串
 88     tupleTime:    时间元组 可通过time.localtime() or datetime.datetime.now().timetuple()获取 默认当前时间的元组
 89     return:       Mon May 13 11:27:42 2019 -> str
 90     """
 91     return time.asctime(tupleTime)
 92
 93
 94 def sleepTime():
 95     """
 96     description:  推迟调用线程的运行
 97     """
 98     for i in range(4):
 99         print(i)
100         time.sleep(3)
101
102
103 # ======================
104 # ====== datetime ======
105 # ======================
106
107
108 def getNowDateTime():
109     """
110     description:  获取当前日期&时间
111     return:       2019-05-13 14:41:15 -> str
112     """
113     timestamps = str(datetime.datetime.now()).split(".")[0]
114     return timestamps
115
116
117 def getNowTime():
118     """
119     description:  获取当前时间
120     return:       14:41:15 -> str
121     """
122     timestamps = str(datetime.datetime.now().time()).split(".")[0]
123     return timestamps
124
125
126 def getTodayDate():
127     """
128     description:  获取当前日期
129     return:       2019-05-13 -> str
130     tipe:         datetime.datetime.now().date()有相同效果
131     """
132     timestamps = str(datetime.date.today())
133     return timestamps
134
135
136 def getTimeDate(times=time.time()):
137     """
138     description:  获取指定时间戳的日期
139     time:         秒 默认当前时间
140     return:       2019-05-13 -> str
141     tips:         一天86400秒
142     """
143     timestamps = str(datetime.date.fromtimestamp(round(times)))
144     return timestamps
145
146
147 # 获取距离现在时间的任意时间的日期     正数 加,负数 减  return:2019-05-12
148 def getAnyDateTime(day, hour=0, min=0, sec=0):
149     """
150     description:  获取距离现在时间的任意时间的日期&时间
151     day:          天数 1代表当前时间+1天    -1代表当前时间-1天
152     hour:         小时 2代表当前时间+2h     -2代表当前时间-2h     默认=0
153     min:          分钟 30代表当前时间+30min -30代表当前时间-30m   默认=0
154     sec:          秒   120代表当前时间+120s -120代表当前时间-120s 默认=0
155     return:       2019-05-15 15:37:41 -> str
156     """
157     return str(datetime.datetime.now() + datetime.timedelta(days=day, hours=hour, minutes=min, seconds=sec)).split(".")[0]
158
159
160 def getAnyDateSecondTime(day, hour=0, min=0, sec=0):
161     """
162     description:  获取距离现在时间的任意时间的秒数
163     day:          天数 1代表当前时间+1天    -1代表当前时间-1天
164     hour:         小时 2代表当前时间+2h     -2代表当前时间-2h     默认=0
165     min:          分钟 30代表当前时间+30min -30代表当前时间-30m   默认=0
166     sec:          秒   120代表当前时间+120s -120代表当前时间-120s 默认=0
167     return:       1557902182 -> str
168     """
169     anyDay = datetime.datetime.now() + datetime.timedelta(days=day, hours=hour, minutes=min, seconds=sec)
170     return str(round(time.mktime(anyDay.timetuple())))
171
172
173 def getTodayTime():
174     """
175     description:  获取当天0点的时间戳
176     return:       1557676800 -> str
177     """
178     return str(round(time.mktime(datetime.date.today().timetuple())))
179
180
181 def getCurrentWeekTime():
182     """
183     description:  获取本周周一0点
184     return:       1557676800 -> str
185     tips:         可替换成: timestamps = time.mktime(time.strptime(time.strftime("%Y-%m-%d", time.localtime(times)), "%Y-%m-%d"))
186     """
187     week = int(time.strftime("%w", time.localtime()))
188     times = round(time.time()) - (week - 1) * 86400
189     timestamps = time.mktime(datetime.date.fromtimestamp(times).timetuple())
190     return str(round(timestamps))
191
192
193 def test():
194     print(getCurrentMilliSecondTime())
195     print(getCurrentSecondTime())
196     print(getCurrentFormatTimeStr())
197     print(getCurrentTimeTupleByFormatStr())
198     print("=======")
199     print(getCurrentTimeStr())
200     print(getCurrentTimeStrByTuple(time.localtime()))
201     print(getTimeByTuple(time.localtime()))
202     print("=======")
203     print(getNowDateTime())
204     print(getNowTime())
205     print(getNowDateTime())
206     print(getTodayDate())
207     print(getTimeDate(time.time() - 86400))
208     print("=======")
209     print(getAnyDateTime(2))
210     print(getAnyDateSecondTime(2))
211     print("=======")
212     print(getTodayTime())
213     print(getCurrentWeekTime())
214
215
216 if __name__ == '__main__':
217     print(test())