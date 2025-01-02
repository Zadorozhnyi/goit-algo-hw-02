from collections import deque

def is_palindrome(input_string: str) -> bool:
    # Перевіряє, чи є переданий рядок паліндромом.
    # - Нечутливо до регістру (усі літери зводить до нижнього).
    # - Ігнорує пробіли.
    # Повертає True, якщо рядок є паліндромом, і False – якщо ні.

    # Перетворення рядка в нижній регістр і видалення пробілів
    normalized_string = input_string.lower().replace(" ", "")
    
    # Створюємо двосторонню чергу (deque) з усіх символів обробленого рядка
    char_deque = deque(normalized_string)
    
    # Порівнюємо символи з обох кінців
    while len(char_deque) > 1:
        left_char = char_deque.popleft()
        right_char = char_deque.pop()
        if left_char != right_char:
            return False
    return True

def main():
    # Тести для демонстрації
    test_strings = [
        "A nut for a jar of tuna",
        "Madam",
        "Step on no pets",
        "Hello",
        "Was it a car or a cat I saw",
        "No lemon, no melon"
    ]
    
    for s in test_strings:
        result = is_palindrome(s)
        print(f"Рядок: '{s}' -> Паліндром? {result}")

if __name__ == "__main__":
    main()
