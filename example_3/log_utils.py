from typing import List, Dict

def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    """
    Фільтрує логи за рівнем.
    """
    return [log for log in logs if log["level"] == level]

def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Рахує кількість записів для кожного рівня логування.
    """
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts

def display_log_counts(counts: Dict[str, int]):
    """
    Виводить статистику кількості записів за рівнями.
    """
    print(f"{'Рівень логування':<18} | {'Кількість':<8}")
    print("-" * 30)
    for level, count in sorted(counts.items()):
        print(f"{level:<18} | {count:<8}")
