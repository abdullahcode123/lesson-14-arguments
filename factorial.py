def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print("Factorial._________doc________")
print("The factorial of 0 is",factorial(0))
print("The factorial of 4 is",factorial(4))
print("The factorial of 5 is",factorial(5))
print("The factorial of 10 is",factorial(10))