def add(a, b):
    """Складывает два числа"""
    return a + b

def subtract(a, b):
    """Вычитает b из a"""
    return a - b

# Тестируем сразу
if __name__ == "__main__":
    print("Тест калькулятора:")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")