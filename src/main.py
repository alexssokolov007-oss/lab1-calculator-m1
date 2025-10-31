from src.costants import OPERATIONS
from src.calculator import calculate_expression

def main() -> float | str:
    expr = input()
    
    try:
        result = calculate_expression(expr)
        print(result)
        return result
    except Exception:
        print("Ошибка")
        return "Ошибка"

if __name__ == "__main__":
    main()
