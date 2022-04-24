
# from turtle import width


# def greet(name):
#     print(f"hello {name}")
#     print(f"how are you {name}")


# greet("abhinav")


# def greet_with_arg(name, location):
#     print(f"who the fuck this {name} is?")
#     print(f"he is from {location}")


# greet_with_arg("abhinav", "patna")


# def greet_with_kwarg(a, b, c):
#     print(f"who the fuck this {b} is?")
#     print(f"he is from {c}")
#     print(f"this is from {a}")

# greet_with_kwarg(a="abhi", b="abhinav", c="ansh")

# from math import ceil


# def paint_calc(height, width, cover):
#     cans = (height * width) / cover
#     print(ceil(cans))


# height = int(input("enter height of the wall: "))
# width = int(input("enter the widt of the wall: "))
# cover = int(input("enter the coverage amount of paint: "))
# paint_calc(height, width, cover)


# prime number checker

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("it is a prime number")
    else:
        print("it's not a prime number")


number = int(input("enter the number to check: "))
prime_checker(number)