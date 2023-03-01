#dict.items()函数
cities = {'CA':'San Francisco','MI': 'Detroit',
'FL': 'Jacksonvill'}
#items函数，将字典的key和value作为元组，返回存在dict_items开始的字典视图特殊序列
cities_it = cities.items()
print(cities_it)
#加list函数后，将字典视图特殊序列转化为列表
cities_li = list(cities.items())
print(cities_li)

#dict_items可用于for循环遍历字典的键和值
for key, value in cities_it:
    print(f"the key is {key}, the value is {value}." )

#items()和list()函数合用，返回列表，用于for循环
for key, value in cities_li:
    print (f"the key is {key}, the value is {value}.")

#dict.get()函数
cities = {'CA':'San Francisco','MI': 'Detroit',
'FL': 'Jacksonvill'}
abbrev = cities.get('CA') #获取对应键的值
print(abbrev)

#若该键不存在,使用get函数不会报错
abbrev_no = cities.get('NI')
print(abbrev_no)

#若该键不存在，可自定义输出内容
#第一种
abbrev_no1 = cities.get('AB')
if not abbrev_no1:
    print("NO EXIT.")
#第二种
abbrev_no1 = cities.get('AB', "Does not exit the key.")
print(abbrev_no1) 

# dict.clear()函数
cities = {'CA':'San Francisco','MI': 'Detroit',
'FL': 'Jacksonvill'}
cities.clear()
print(cities)

#dict.key()函数
cities = {'CA':'San Francisco','MI': 'Detroit',
'FL': 'Jacksonvill'}
print(cities.keys())

#dict.values()函数
cities = {'CA':'San Francisco','MI': 'Detroit',
'FL': 'Jacksonvill'}
print(cities.values())

#dict.pop()函数
cities = {'CA':'San Francisco','MI': 'Detroit',
'FL': 'Jacksonvill'}
print(cities.pop('CA')) #删除除键'CA'及对应值
print(cities)
 #删除键对，若键'NI'不存在，输出'NO Exit'
cities_pop = cities.pop("NI","NO Exit")
print(cities_pop)

#字典排序sorted()函数，及字典的顺序
cities = {'CA':'San Francisco','MI': 'Detroit',
'FL': 'Jacksonvill'}

#for循环遍历字典
print("-" * 20)
for key,value in list(cities.items()):
    print(f"key: {key}, value: {value}")

#按照字典的键排序
print("-" * 20)
cities_s1 = sorted(cities.items(), key= lambda x : x[0]) 
print(cities_s1)

#按照字典的值排序
print("-" * 20)
cities_s2 = sorted(cities.items(), key= lambda x : x[1]) 
print(cities_s2)

#for循环遍历
print("-" * 20)
for key, value in list(cities_s1):
    print(key,value)

print(cities[1])




