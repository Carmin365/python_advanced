def number_generator(n):
    for i in range(n):
        yield i
    for number in number_generator(5):
        print(number) 