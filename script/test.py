def generator():
    n = 0
    for _ in range(10):
        n += 5
        yield n

for n in generator():
    print(n) 
