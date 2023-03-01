#冒泡排序

list1 = [2,6,0,45,8,10,79,30,7]

for i in range(0,len(list1)-1):
    for j in range(0,len(list1)-1):
        if list1[j+1] > list1[j]:
            list1[j],list1[j+1] =list1[j+1],list1[j] 

print(list1)

