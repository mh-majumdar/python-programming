#Convert the tuple into a list to be able to change it
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
y.append("orange") #adding values to tuple
y.remove("cherry") #remove from tuple

x = tuple(y)
print(x)

#Tuple unpacking
fruits = ("apple", "banana", "cherry")
(a, b, c) = fruits

print(a)
print(b)
print(c)

#Loop Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

for i in range(len(thistuple)):
  print(thistuple[i])

i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1