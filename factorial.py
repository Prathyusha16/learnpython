def factorial(num):
    """this factorial calls itself to find the factorial of a number"""
    if num==1:
        return 1
    else:
        return(num*factorial(num-1))
print("factorial of",5,"is:",factorial(5))