#Short Hand If!!!
#If you have only one statement to execute, you can put it on the same line as the statement.if
#Example 
a = 5
b = 2
if a > b: print("a is greater than b") 

#Short Hand If ... Else!!!
#If you have one statement for and one for , you can put them on the same line using a conditional expression:ifelse
#Example
a = 2
b = 330
print("A") if a > b else print("B")

#Assign a Value With If ... Else!!!
#Example
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

#Multiple Conditions on One Line!!!
#Example
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#Practical Examples!!!
#Example 1
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

#Example 2
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)