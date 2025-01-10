list1 = ["abc", 34, True, 40, "male"]
print(list1)
print(len(list1))
print(type(list1))
print(list1[1])
print(list1[2])
print(list1[-1])
print(list1[0:2])   #index 0 included, 2 not included

if 34 in list1:
    print("Yes, Present!")

#List Update
list1[1] = 35
print(list1[1])

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Loop list
list = ["a", "b", "c", "d"]
for x in list:
    print(x, end = " ")
print("")
for i in range(len(list)):
    print(list[i], end = " ")
print("")
i = 0
while i < len(list):
    print(list[i], end=" ")
    i = i + 1

print("")

[print(x) for x in list]

#Join In List:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)