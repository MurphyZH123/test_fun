"""
parse来代替正则表达式

"""
import parse
# # from parse import compile
# from parse import parse
# profile = parse()
# print(profile)
#
# print(type(profile["age"]))
# pattern = compile("I am {}, {} years old, {}")
#
# pattern.parse("I am Jack, 27 years old, male")
# pattern.parse("I am Tom, 26 years old, male")
# flow = 'cookie=0x9816da8e872d717d, duration=298506.364s, table=0, n_packets=480, n_bytes=20160, priority=10,ip,' \
#        'in_port="tapbbdf080b-c2" actions=NORMAL '
#
# result = parse.flow('cookie={cookie}, duration={duration}, table={table}, n_packets={n_packets}, n_bytes={n_bytes}, '
#                     'priority={priority},ip,in_port="{in_port}" actions={actions}')
#
# print(result['duration'])

# print(parse("halo", "hello"))
if parse("halo", "hello") is None:
    print(('结果'))