

def factorial(num):
    """this factorial calls itself to find the factorial of a number"""
    if num==1:
        return 1
    else:
        return(num*factorial(num-1))
#print("factorial of",5,"is:",factorial(5))

def sum_of_two_number(a, b):
    return a+b

def difference_of_two_numbers(a,b) :
    return a-b