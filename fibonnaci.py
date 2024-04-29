def operation(num):
    fib = [0,1]
    while len(fib) < num:
        fib.append(fib[-1] + fib[-2])
    return fib

print(operation(5))