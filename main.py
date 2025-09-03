from calculator import add, subtract  # ← Новая строка

def hello():
    print("Hello from my first project!")

if __name__ == "__main__":
    hello()
    # Тестируем калькулятор
    result = add(5, 3)
    print(f"5 + 3 = {result}")
