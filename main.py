# def fun(n):
#    return n*(n+1)/2
# print(fun(10))

 # activity 02

# def fun2(n):

#     sum=0

#     for i in range(1,n+1):

#         sum+=i

#     return sum

# print(fun2(10))
# activity 03

def fun3(n):

    sum=0

    for i in range(1,n+1):

        for j in range(1,i+1):

            sum+=1

    return sum

print(fun3(10))


