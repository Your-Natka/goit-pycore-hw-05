import sys
from log_parser import load_logs
from log_utils import count_logs_by_level, display_log_counts, filter_logs_by_level

def main():
    """
    Основна точка запуску програми.
    """
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_файлу> [рівень логування]")
        sys.exit(1)

    file_path = sys.argv[1]
    level_filter = sys.argv[2].upper() if len(sys.argv) > 2 else None

    # Завантаження логів
    logs = load_logs(file_path)

    # Підрахунок кількості логів за рівнями
    counts = count_logs_by_level(logs)

    # Вивід статистики
    display_log_counts(counts)

    # Якщо вказано рівень, відображаємо фільтровані логи
    if level_filter:
        filtered_logs = filter_logs_by_level(logs, level_filter)
        if filtered_logs:
            print(f"\nДеталі логів для рівня '{level_filter}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"\nЗаписів рівня '{level_filter}' не знайдено.")

if __name__ == "__main__":
    main()
