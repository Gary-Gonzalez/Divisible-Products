#Gary Gonzalez, HW4 Working with Python Functions, Due October 12
#A function called prodDigits that takes an integer parameter and returns the product of the digits in the integer    
def prodDigits(n):

    product = 1
 
    num = str(n)
     
    for i in num:
        product = product * int(i)
 
    return product

#Calls the prodDigits function to create a list of all numbers from 1 to a given number that are divisible by the product of their digits
def prodDivisible(n):
    
    divList = []
    
    for i in range(1, n):
        c = prodDigits(i)
        if c != 0:
            if i%c == 0:
                divList.append(i)

    return divList




    
