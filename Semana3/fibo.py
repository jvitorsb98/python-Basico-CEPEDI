def fibonacci(N):
    L = [0]
    a, b = 0, 1
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L

print(fibonacci(100000))
