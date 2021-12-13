
def loop1():
    # Sum the odd numbers between 1 and 20
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    return odd_sum
print(loop1())


def loop2():
    # Sum the even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum
print(loop2())


def loop1Rec(num,odd_sum):
    # Duplicate the loop1 function using recursion
    if num == 20: #Loop is stopping once num reaches 20
        return odd_sum
    else:
        if num % 2 == 1: #Check to see if number is odd
            odd_sum += num
        return(loop1Rec(num+1, odd_sum)) #Calling function again and adding 1 to starting number.
print(loop1Rec(0,0))
                

def loop2Rec(num,even_sum):
    # Duplicate the loop2 function using recursion
    if num == 20: #Loop is stopping once num reaches 20
        return even_sum
    else:
        if num % 2 == 0: #Check to see if number is even
            even_sum += num
        return(loop2Rec(num+1, even_sum)) #Calling function again and adding 1 to starting number.
print(loop2Rec(0,0))