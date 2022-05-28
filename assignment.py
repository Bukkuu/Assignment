list1=[15,21,6,78,30]
print("Smallest number is:",min(list1))

l1 = ["Hire", "the", "top", "1%", "freelancers"]
l2 = []
if len(l2):
    print("list is not empty")
else:
    print("list is empty")


import random
fruits_list = ['apple','orange', 'pear','mango', 'papaya']
print(random.choice(fruits_list))

data = ["Sristy", "Shanti", 19]
data2 = []
data2 = data.copy()
print(data)
print(data2)

list1 = [15,21,6,78,30]
print("Second largest number is:", sorted(list1)[-2])

fruit = ['apple','orange', 'pear','mango', 'papaya']
fruit = [x for (i,x) in enumerate(fruit) if i not in (2,5)]
print(fruit)

list1 = [15,21,6,78,30]
even_count, odd_count = 0,0
for num in list1:
    if num % 2 == 0:
        even_count += 1
else:
    odd_count += 2
print("Even numbers in the list:",even_count)
print("odd numbers in the list:",odd_count)

Tuple1=("Apple","Ball","Cat")
print("original tuple", Tuple1)
List1= list(Tuple1)

Tuple1=("Apple","Ball","Cat")
print("original tuple", Tuple1)
List1= list(Tuple1)
print("original list",List1)
List1.insert(3,"Dog")
print("changed list",List1)
Tuple2=tuple(List1)
print("adding new name in tuple",Tuple2)

Tuple= (False,19,"Python")
List = list(Tuple)
print(type(List))
print(List)

tup = ('p','y','t','h','o','n')
str = ''.join(tup)
print(str)

def convert(list):
    return tuple(list)
list=[0,1,2,3,4]
print(convert(list))

ini_list = [{'a':[0,1,2,3],'b':[6,7,8]},{'c':[20,21,25],'d':[61,65,69]}]
dict_list = [(key, )+tuple(val)for dic in ini_list for key, val in dic.items()]
print("Resultant list of tuples:{}".format(dict_list))

