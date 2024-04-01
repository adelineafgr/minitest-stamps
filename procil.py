def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def foo_bar(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FooBar"
    elif num % 3 == 0:
        return "Foo"
    elif num % 5 == 0:
        return "Bar"
    else:
        return str(num)

numbers = list(range(1, 101))
numbers.reverse()

for num in numbers:
    if is_prime(num):
        continue
    print(foo_bar(num), end=" ")
