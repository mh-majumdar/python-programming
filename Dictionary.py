d = {
  "year": 2020,
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(d)
print(len(d))

#Accessing Items
x = d["year"]
print(x)
y = d.keys()
print(y)
z = d.values()
print(z)

#Change vales
d["year"] = 2024
d["owner"] = "mehedi"
print(d)
d.popitem()
print(d)
d.pop("year")
print(d)

#Loop dictionar
for x in d:
   print(x)    #print only keys

for x in d:
   print(d[x]) #print only values

for i, j in d.items():
   print(i, j) #print keys and values

#Nested Dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])