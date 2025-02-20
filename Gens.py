def squares_up_to_n(N):
    for i in range(1, N + 1):
        yield i ** 2

N = 8
for square in squares_up_to_n(N):
    print(square)


def evensToN(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))
even_numbers = evensToN(n)
print(", ".join(map(str, even_numbers)))


def divisibleBy3n4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = 50
for num in divisibleBy3n4(n):
    print(num)

def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

for square in squares(2, 8):
    print(square)


def countdown(n):
    while n >= 0:
        yield n
        n -= 1

for num in countdown(10):
    print(num)
