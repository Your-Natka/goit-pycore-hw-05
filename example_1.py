def caching_fibonacci():
    # Створюємо порожній словник для кешування
    cache = {}

    def fibonacci(n):
        """Обчислює n-те число Фібоначчі з використанням кешування."""
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        # Перевіряємо, чи є результат у кеші
        if n in cache:
            return cache[n]

        # Якщо результату немає в кеші, обчислюємо його
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Повертаємо внутрішню функцію
    return fibonacci


# Приклад використання
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
