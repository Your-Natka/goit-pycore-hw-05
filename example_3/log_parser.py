import sys
from typing import List, Dict

def parse_log_line(line: str) -> Dict[str, str]:
    """
    Парсить один рядок лог-файлу.
    """
    parts = line.split(" ", 3)  # Розділяємо на 4 частини: дата, час, рівень, повідомлення
    if len(parts) < 4:
        raise ValueError(f"Некоректний формат логу: {line}")
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3].strip()
    }

def load_logs(file_path: str) -> List[Dict[str, str]]:
    """
    Завантажує лог-файл і парсить кожен рядок.
    """
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():  # Пропускаємо порожні рядки
                    logs.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"Помилка: Файл {file_path} не знайдено.")
        sys.exit(1)
    except ValueError as e:
        print(f"Помилка обробки логу: {e}")
        sys.exit(1)
    return logs
