# create a mapping of state to abbreviation
#创建一个州与缩写的映射
states = {'Oregon':'OR','Florida':'FL','California': 'CA',
'New York': 'NY','Michigan':'MI'} #创建一个字典，key为州名，value为州缩写

#Create a basic set of states and some cities in them
#创造一系列州与其中的一些城市
cities = {'CA':'San Francisco','MI': 'Detroit',
'FL': 'Jacksonvill'} #创建字典，key为州缩写，value为城市

#add some more cities
#增加更多的城市
cities['NY'] = 'New York' #添加cities字典的key为NY,value为New York
cities['OR'] = 'Portland' #添加cities字典的key为OR，value为Portland

#print out some cities 打印一些城市
print('-' * 10)
print("NY State has: ",cities['NY']) #通过cities字典的key为NY，打印对应Value
print("OR State has: ",cities['OR']) #同上

#print some states 打印一些州
print('-' * 10)
print("Michigan's abbreviation is: ",states['Michigan']) #通过字典states的key'Michigan'，打印对应的Value
print("Florida's abbreviation is: ",states['Florida']) #同上

#do it by using the state then cities dict
# 通过使用州和城市的字典来打印
print('-' * 10) 
print("Michigan has: ",cities[states['Michigan']]) 
#step1，通过states字典的key 'Michigan'找到对应的value 'MI'；step2，'MI'又作为cities字典的key，打印对应的value 'Detroit'。
print("Florida has: ",cities[states['Florida']]) #原理同上

# print every state abbreviation 打印每个州的缩写
print('-' * 10)
#items()函数以列表返回可遍历的（键值）元组数组。列表内为元组，元组内包含了字典的key和value
for state,abbrev in list(states.items()): 
#items()函数以列表返回可遍历的（键值）元组数组。列表内为元组，元组内包含了字典的key和value
    print(f"{state} is abbreviated {abbrev}")

#print every city in states
print('-' * 10)
#for循环遍历字典，items()将字典转化为字典视图特殊序列
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time 同时打印所以州和城市
print('-' * 10)
#for循环遍历字典，items()将字典转化为字典视图特殊序列
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)

# safely get a abbreviation by state that might not be there
#安全的获得一个可能不存在的州的缩写
state = states.get('Texas') #get()函数，获取指定键对应的值，若键不存在，则可自定义输出值，不会报错。

if not state:
    print("Sorry, no Texas.")

#get a city with a default value 获得一个城市的默认值
city = cities.get('TX', 'Does Not Exist') #获取不存在的州缩写，并自定义输出元素，且不报错
print(f"The city for the state 'TX' is {city}")

