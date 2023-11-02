def f(x):
    y = x**2 + 2*x + 3
    return y

t = int(input())
print(f(f(f(t)+t)+f(f(t))))