def parse_text(value):
    if value is None or value.strip() == "":
        return None
    return value.strip()

def parse_int(value):
    if value is None or value.strip() == "":
        return None
    cleaned_value = value.strip()
    try:
        return int(cleaned_value)
    except ValueError:
        raise ValueError(f"'{value}' не подходит")

def parse_date(value):
    if value is None or value.strip() == "":
        return None
    cleaned_value = value.strip()
    try:
        day, month, year = map(int, cleaned_value.split('.'))
        return (day, month, year)
    except ValueError:
        raise ValueError(f"'{value}' это не дата")
    
    



def required(value):
    if value is None:
        return False 
    return (True, "")

def not_empty(value):
    if value is not None and len(value.strip()) == 0:
        return False
    return (True, "")

def min_length(min_len):
    def validator(value):
        if value is not None and len(value) < min_len:
            return False
        return (True, "")
    return validator

def max_length(max_len):
    def validator(value):
        if value is not None and len(value) > max_len:
            return False
        return (True, "")
    return validator

def min_value(min_val):
    def validator(value):
        if value is not None and value < min_val:
            return False
        return (True, "")
    return validator

def max_value(max_val):
    def validator(value):
        if value is not None and value > max_val:
            return False
        return (True, "")
    return validator





import re
from datetime import datetime
def phone(value):
    if value is None:
        return (True, "")
    pattern = r'^\+7\d{10}$'
    if not re.match(pattern, value):
        return False
    return (True, "")

def email(value):
    if value is None:
        return (True, "") 
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, value):
        return False
    return (True, "")

def past(value):
    if value is None:
        return (True, "")
    day, month, year = value
    input_date = datetime(year, month, day)
    today = datetime.now()
    if input_date >= today:
        return False
    return (True, "")

def future(value):
    if value is None:
        return (True, "")
    day, month, year = value
    input_date = datetime(year, month, day)
    today = datetime.now()
    if input_date <= today:
        return False
    return (True, "")








"ПРОВЕРКА ОДНОГО ПОЛЯ!!!!!!"

def check_age():
    """Проверяет возраст пользователя"""
    print("=" * 30)
    print("ПРОВЕРКА ВОЗРАСТА")
    print("=" * 30)
    age_input = input("Введите ваш возраст: ").strip()
    if not age_input:
        print(" ОШИБКА: Возраст не может быть пустым!")
        return (False,None)
    if not age_input.isdigit():
        print(f" ОШИБКА: '{age_input}' не является числом!")
        return (False,None)
    age = int(age_input)
    if age < 0:
        print("ОШИБКА: Такого не может быть")
        return (False,None)
    elif age < 18:
        print(" ОШИБКА: Вам должно быть больше 18")
        return (False,None)
    elif age > 120:
        print("ОШИБКА: Возраст должен быть  до 120 лет")
        return (False,None)
    print(f"ВОЗРАСТ {age} ПРИНЯТ!")
    if age >= 18:
        print("Доступ разрешен.")
    return (True, age)
if __name__ == "__main__":
    success, age_value = check_age()
    if success:
        print(f"\n Проверка пройдена успешно!")
        print(f"Возраст пользователя: {age_value} лет")
    else:
        print("\n Пожалуйста введитеьт возраст.")






"ПРОВЕРКА НЕСКОЛЬКИХ ПОЛЕЙ!!!!!1"
import re
def validate_age(age_value):
    if not age_value or str(age_value).strip() == "":
        return False
    try:
        age = int(str(age_value).strip())
    except ValueError:
        return False 
    if age < 18:
        return (False, "Минимальный возраст: 18 лет")
    elif age > 120:
        return (False, "Максимальный возраст: 120 лет")
    return (True, age)
def validate_phone(phone_value):
    if not phone_value or str(phone_value).strip() == "":
        return (True, None)
    phone = str(phone_value).strip()
    if not phone.startswith("+7"):
        return (False, "Телефон должен начинаться с +7")
    if len(phone) != 12:
        return (False, "Телефон должен содержать 12 символов")
    if not phone[2:].isdigit():
        return (False, "После +7 должны быть только цифры")
    return True, phone
def validate_form():
    print("=" * 50)
    print("Документ")
    print("=" * 50)
    errors = {} 
    user_data = {} 
    print("\n ВОЗРАСТ ")
    age_input = input("Введите ваш возраст:").strip()
    age_ok, age_result = validate_age(age_input)
    if age_ok:
        user_data["age"] = age_result  
        print(f"Возраст: {age_result} лет")
    else:
        errors["age"] = age_result
        print(f"Ошибка возраста: {age_result}")
    print("\n ТЕЛЕФОН ")
    print("(Можно оставить пустым)")
    phone_input = input("Введите телефон:").strip()
    phone_ok, phone_result = validate_phone(phone_input)
    if phone_ok:
        if phone_result is not None:
            user_data["phone"] = phone_result
            print(f"Телефон: {phone_result}")
        else:
            print("Телефон не указан")
    else:
        errors["phone"] = phone_result
        print(f"Ошибка телефона: {phone_result}")
    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТ ПРОВЕРКИ")
    print("=" * 50)
    if errors:
        print("\n ОБНАРУЖЕНЫ ОШИБКИ:")
        for field, error in errors.items():
            print(f" {field}: {error}")
        print("\n Пожалуйста исправьте ошибки")
        return False, errors, user_data
    else:
        print("\n ВСЕ ДАННЫЕ ВЕРНЫ!")
        print("\n СОХРАНЕННЫЕ ДАННЫЕ:")
        print(f"  Возраст: {user_data.get('age')} лет")
        print(f"  Телефон: {user_data.get('phone', 'не указан')}")
        return True, None, user_data
if __name__ == "__main__":
    success, errors, data = validate_form()
    if success:
        print("\n" + "=" * 50)
        print("РЕГИСТРАЦИЯ УСПЕШНА!")
        age = data["age"]
        phone = data.get("phone")  
        print(f"\nВозраст пользователя: {age}")
        if phone:
            print(f"Телефон: {phone}")
        if age >= 18 and age < 30:
            print("Категория: Молодые")
        elif age >= 30 and age < 60:
            print("Категория: Взрослые")
        elif age >= 60:
            print("Категория: Старые")