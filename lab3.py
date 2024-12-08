import warnings
warnings.filterwarnings("ignore")

import re

def validate_card_number(card_number):
    # Паттерн для проверки формата номера карты
    pattern = r'^(?:(\d{4}[- ]?){3}\d{4})$'
    return re.fullmatch(pattern, card_number) is not None

def find_card_numbers_in_text(text):
    # Паттерн для поиска номеров карт в тексте
    pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'
    return re.findall(pattern, text)

def find_card_numbers_in_file(file_path): 
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if content.strip():  # Проверяем, что файл не пуст
                return find_card_numbers_in_text(content)
            else:
                print(f"Файл {file_path} пуст.")
                return []
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return []