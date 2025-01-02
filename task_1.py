import queue
import time
import random

# Створюємо глобальну чергу заявок
requests_queue = queue.Queue()

def generate_request():
    # Генерує нову заявку з унікальним ідентифікатором та додає її до черги.
    # Для прикладу генеруємо ID заявки випадковим чином
    request_id = random.randint(1000, 9999)
    requests_queue.put(request_id)
    print(f"[INFO] Заявка з ID {request_id} додана в чергу.")

def process_request():
    # Обробляє одну заявку з черги (якщо вона не порожня), імітуючи роботу сервісного центру.
    if not requests_queue.empty():
        current_request = requests_queue.get()  # дістаємо заявку з черги
        print(f"[INFO] Обробка заявки з ID {current_request}...")

        # імітуємо затримку в обробці
        time.sleep(1)  
        print(f"[INFO] Заявка {current_request} успішно оброблена.")
    else:
        print("[WARN] Черга порожня. Немає заявок для обробки.")

def main():
    # Головна функція, яка ініціює нескінченний цикл:
    # - генерує нові заявки;
    # - відразу пробує обробити одну заявку;
    # - робить невелику затримку перед повторенням.
    # Натисніть Ctrl+C, щоб зупинити програму.

    print("Початок роботи системи обробки заявок. Натисніть Ctrl+C для виходу.")
    try:
        while True:
            # Генеруємо випадкову кількість заявок (наприклад, 0..2) за ітерацію
            for _ in range(random.randint(0, 2)):
                generate_request()

            # Обробляємо принаймні одну заявку за ітерацію
            process_request()

            # Невелика затримка, щоб краще спостерігати за процесом
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[INFO] Завершення роботи програми...")

if __name__ == "__main__":
    main()
