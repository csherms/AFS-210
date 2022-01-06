def fib(n): 
    if n <= 2: 
        return 1 
    else: 
        return fib(n-1) + fib(n-2)
        
        
print(fib(16))


# def dyna_fib(n, lookup): 
#     if n <= 2: 
#         lookup[n] = 1 

#     if lookup[n] is None: 
#         lookup[n] = dyna_fib(n-1, lookup) + dyna_fib(n-2, lookup) 

#     return lookup[n]

# print(dyna_fib(5,2))