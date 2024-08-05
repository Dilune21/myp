def fibonacci_ate_2000():
    a, b = 0, 1
    while a <= 2000:
        print(a, end=" ")
        a, b = b, a + b

if __name__ == "_main_":
    fibonacci_ate_2000()