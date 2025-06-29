import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None] :
    """
    Генератор, що знаходить усі дійсні числа у тексті.

    :param text: Вхідний текст, у якому потрібно знайти числа.
    :yield: Дійсне число, знайдене у тексті.
    """
    # Використовуємо регулярний вираз для пошуку чисел
    for match in re.finditer(r'(?<=\s)\d+(\.\d+)?(?=\s)', text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Обчислює загальну суму чисел у тексті за допомогою генератора.

    :param text: Вхідний текст із числами.
    :param func: Функція, яка повертає генератор чисел із тексту.
    :return: Сума всіх чисел у тексті.
    """
    return sum(func(text))


# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")
