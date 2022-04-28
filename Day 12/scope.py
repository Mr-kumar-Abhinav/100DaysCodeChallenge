# concept of local, global scope and variable:

global_variable = "abhinav "
def greet():
    local_variable = "kumar"  
    print(f"this is local {local_variable}")

greet()
print(f"this is global {global_variable}")


# Modifing global scope. but one must avoid modifing global scope within a function that has a local scope.
def greet():
    global global_variable  # global variable can be accessed inside a local scope using "global" keyword.
    global_variable += "anshu"
    print(f"{global_variable} is modified global variable which you hv accessed inside local scope")

greet()
print(f"{global_variable}") # this will print modified global_variable ie. abhinav anshu


# example

i = 100
def num():
    i = 200
    return i


num()
print(i) # this will print 100 because i = 100 is in global scope and i inside the function num() is in local scope. to print i = 200 we have to put the word global inside the num() function.