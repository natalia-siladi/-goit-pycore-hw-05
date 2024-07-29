def caching_fibonacci():
    cashe = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cashe:
            return cashe[n]
        
        result = fibonacci(n - 1) + fibonacci(n - 2)
        cashe[n] = result

        return result
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610

