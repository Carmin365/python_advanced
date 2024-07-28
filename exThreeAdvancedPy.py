def num_generator(n):
    for i in range(n):
        yield i
    for num in num_generator(5):
        print(num) 
