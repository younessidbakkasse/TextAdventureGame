def function(num):
    res = [num%i for i in range(2, int(num/2 + 1))]
    return not(0 in res)

print(function(3))