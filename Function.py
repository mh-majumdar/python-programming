def fun():     #function strucrure
    print("This is a fun of function")

fun()          #function call

def my_function(f):
  print(f + " Hasan")

my_function("Mehedi")

#Arbitrary Arguments, *args

def arb_fun(*name):
   print(name)

arb_fun("Mehedi", "Hasan")

#Keyword Arguments
def my_function(fname, lname):
  print("The lname child is " + lname)

my_function(fname= "Mehedi", lname = "Hasan")

#Passing a List as an Argument
def fun_list(l):
   for x in l:
      print(x)

y = [1, 2, 3]

fun_list(y)

#Passing a List as an Argument
def my_function(x, /):
  print(x)

my_function(10)
   
   