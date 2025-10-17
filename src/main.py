from src.costants import OPERATIONS
from calculator.calculator import calculate_expression


def main() -> float | str:
    """
    Основная функция: читает выражение, вычисляет результат и выводит его
    Возвращает результат или 'Ошибка!' при исключении
    """
    expression: str = str(input())
    try:
        result: float = calculate_expression(expression)
    except Exception as e:
        print(e)
        return 'Ошибка!'
    print(result)
    return result


if __name__ == "__main__":
    main()
