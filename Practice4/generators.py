#Exercice 1: Create a generator that generates the squares of numbers up to some number N
def squares_up_to(N):
    for i in range(N + 1):
        yield i**2
        
for sq in squares_up_to(5):
    print(sq, end=' ')  # output: 0 1 4 9 16 25
    
#Exercice 2: Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter n: "))
print(', '.join(str(x) for x in even_numbers(n)))

#Exercice 3: Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for num in divisible_by_3_and_4(30):
    print(num, end=' ')  # output: 0 12 24

#Exercise 4: Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    for i in range(a, b + 1):
        yield i**2

for sq in squares(3, 7):
    print(sq, end=' ')  # output: 9 16 25 36 49
    
#Exercise 5: Implement a generator that returns all numbers from (n) down to 0.
def countdown(n):
    for i in range(n, -1, -1):
        yield i

for num in countdown(5):
    print(num, end=' ')  # output: 5 4 3 2 1 0