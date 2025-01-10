# Since the try block raises an error, the except block will be executed.
# Without the try block, the program will crash and raise an error.

try:
  print(x)
except:
  print("An exception occurred")

# You can define as many exception blocks as you want, e.g.
# if you want to execute a special block of code for a special kind of error.

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# You can use the else keyword to define
# a block of code to be executed if no errors were raised

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#The finally block, if specified,
# will be executed regardless if the try block raises an error or not.

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")