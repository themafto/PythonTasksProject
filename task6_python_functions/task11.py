def generator_squares(n):
    for i in range(n+1):
        yield i * i

print(list(generator_squares(5)))
print(sum(generator_squares(4)))