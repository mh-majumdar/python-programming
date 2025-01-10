#Quotes Inside Quotes
print("It's alright")
print("He is called 'Mehedi'")
print('He is called "Mehedi"')

#Multiline String
a = "I am Mehedi Hasan"
print(a)

#String Index Accessing
b = "Mehedi"
print(b[0])

for x in "Python":
    print(x, end="")

print("")
#String Slicing
c = "Ilovepython"
print(c[0:4])
print(c[:4])
print(c[4:])
print(b[-1:-2])

#Convertion
d = "mehedi hasan"
print(d.upper())
print(d.lower())
print(d.strip())
print(d.replace("m","x"))
print(d.split(","))

#String Concatation
a = "Hello"
b = "world"
print(a+b)
print(a + " " + b)

#String Format
# age = 36
# txt = "My name is X, I am " + age
# print(txt)

age = 36
txt = f"My name is X, I am {age:.2f}"
print(txt)

#Escape Character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)