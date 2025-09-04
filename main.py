from calculator import add, subtract # ← Новая строка

def hello():
    print('hello from my first project!')


if __name__ == "__main__":
    hello()
    # Тестируем калькулятор
    result = add(5, 5)
    print(f"5 + 5 = {result}")
