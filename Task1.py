import queue
import threading
import time
import random

# Глобальна черга для зберігання заявок
request_queue = queue.Queue()

def generate_request():
    # Створення нової заявки
    request_id = random.randint(1000, 9999)
    request_data = f"Request {request_id}"
    
    # Додання заявки до черги
    request_queue.put(request_data)
    print(f"Generated: {request_data}")

def process_request():
    # Якщо черга не пуста
    if not request_queue.empty():
        # Видалення заявки з черги
        request_data = request_queue.get()
        
        # Обробленя заявки
        print(f"Processing: {request_data}")
        time.sleep(random.uniform(1, 2)) 
        request_queue.task_done()
        print(f"Processed: {request_data}")
    else:
        # Виведенря повідомлення, що черга пуста
        print("Queue is empty")

def main_loop():
    try:
        while True:
            # Виконання generate_request() для створення нових заявок
            generate_request()
            
            # Виконання process_request() для обробки заявок
            process_request()
            
            # Затримка для імітації реального часу між операціями
            time.sleep(random.uniform(0.5, 1.5))
    except KeyboardInterrupt:
        print("Exiting program...")

if __name__ == "__main__":
    main_loop()
