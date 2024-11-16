"""TASK 1"""
def check_positive(number):

    if number <= 0:
        raise ValueError("Число должно быть положительным.")
def check_non_empty_string(text):

    if not text:
        raise ValueError("Строка не должна быть пустой.")
"""TASK 2"""
def check_positive_numbers(*args):
    try:
        for number in args:
            if not isinstance(number, (int, float)) or number <= 0:
                raise ValueError(f"Некорректное значение: {number}. Все параметры должны быть положительными числами.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        with open("error_log.txt", "a") as log_file:
            log_file.write(f"Ошибка: {e}\n")
"""TASK 3"""
def validate_parameters(*args):
    try:
        for param in args:
            if param == 0:
                raise ValueError("Параметр не должен быть равен 0.")
            if not isinstance(param, (int, float)):
                raise ValueError("Все параметры должны быть числами.")
        print("Все параметры корректны и проходят валидацию.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        with open("error_log.txt", "a") as log_file:
            log_file.write(f"Ошибка: {e}\n")

    finally:
        print("Завершение работы функции validate_parameters.")
"""TASK 4"""
def validate_positive_numbers(*args):
    try:
        for param in args:
            if param <= 0:
                raise ValueError("Все параметры должны быть положительными числами.")
            if not isinstance(param, (int, float)):
                raise TypeError("Все параметры должны быть числом (int или float).")
        
        print("Все параметры корректны и положительны.")

    except ValueError as ve:
        print(f"Ошибка валидации: {ve}")
        with open("value_error_log.txt", "a") as log_file:
            log_file.write(f"ValueError: {ve}\n")

    except TypeError as te:
        print(f"Ошибка типа: {te}")
        with open("type_error_log.txt", "a") as log_file:
            log_file.write(f"TypeError: {te}\n")

    except Exception as e:
        print(f"Общая ошибка: {e}")

    finally:
        print("Завершение работы функции validate_positive_numbers.")
def calculate_average(*args):

    try:
        if len(args) == 0:
            raise ZeroDivisionError("Нет параметров для вычисления среднего.")
        
        total = 0
        count = 0
        
        for param in args:
            if not isinstance(param, (int, float)):
                raise ValueError("Все параметры должны быть числом (int или float).")
            total += param
            count += 1
        
        average = total / count
        print(f"Среднее значение: {average}")

    except ZeroDivisionError as zde:
        print(f"Ошибка деления на ноль: {zde}")

    except ValueError as ve:
        print(f"Ошибка валидации: {ve}")

    except Exception as e:
        print(f"Общая ошибка: {e}")

    finally:
        print("Завершение работы функции calculate_average.")
def remove_item_from_list(item, input_list):

    try:
        if not isinstance(input_list, list):
            raise TypeError("input_list должен быть списком.")
        
        if item not in input_list:
            raise ValueError("Элемент не найден в списке.")
        
        input_list.remove(item)
        print(f"Элемент {item} успешно удален.")

    except TypeError as te:
        print(f"Ошибка типа: {te}")

    except ValueError as ve:
        print(f"Ошибка валидации: {ve}")
    
    except Exception as e:
        print(f"Общая ошибка: {e}")

    finally:
        print("Завершение работы функции remove_item_from_list.")
"""TASK 5"""
def process_numbers(*args):
    
    try:
        for number in args:
            if not isinstance(number, int):
                raise TypeError(f"Параметр '{number}' не является целым числом.")
            if number <= 0:
                raise ValueError(f"Параметр '{number}' не является положительным числом.")

        print("Все параметры корректны!")

    except ValueError as ve:
        print(f"Ошибка валидации значений: {ve}")
        with open("value_error_log.txt", "a") as log_file:
            log_file.write(f"ValueError: {ve}\n")

    except TypeError as te:
        print(f"Ошибка типа: {te}")
        with open("type_error_log.txt", "a") as log_file:
            log_file.write(f"TypeError: {te}\n")

    finally:
        print("Функция завершила выполнение.")
"""TASK 6"""
class NegativeNumberError(Exception):
    pass
def check_positive_1(number):
        if number < 0:
            raise NegativeNumberError(f"Число {number} отрицательное. Ожидалось положительное число.")
class NotAnIntegerError(Exception):
    pass
def check_integer(value):
    if not isinstance(value, int):
        raise NotAnIntegerError(f"Значение '{value}' не является целым числом.")
class ValueOutOfRangeError(Exception):
    pass
def check_range(value, min_value, max_value):
    if not (min_value <= value <= max_value):
        raise ValueOutOfRangeError(f"Значение {value} должно быть в диапазоне [{min_value}, {max_value}].")
"""TASK 7"""  
class ValueOutOfRangeErrorr(Exception):
    pass
def process_values(*args):
    try:
        for value in args:
            if value < 0 or value > 100:
                raise ValueOutOfRangeErrorr(f"Значение {value} выходит за пределы допустимого диапазона (0-100).")
            print(f"Обрабатываю значение: {value}")
    except ValueOutOfRangeErrorr as e:
        print(f"Обработано исключение: {e}")
        with open("error_log.txt", "a") as log_file:
            log_file.write(str(e) + "\n")
    finally:
        print("Завершение обработки значений.")
"""TASK 8"""
class DivisionByZeroError(Exception):
    pass
def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise DivisionByZeroError("Деление на нуль запрещено.")
        result = numerator / denominator
        print(f"Результат деления: {result}")
        return result
    except DivisionByZeroError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Завершение операции деления.")
class IndexOutOfRangeError(Exception):
    pass
def get_char_from_string(string, index):
    try:
        if index < 0 or index >= len(string):
            raise IndexOutOfRangeError(f"Индекс {index} выходит за пределы длины строки.")
        char = string[index]
        print(f"Символ по индексу {index}: {char}")
        return char
    except IndexOutOfRangeError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Завершение работы с индексом строки.")
class InvalidFormatError(Exception):
    pass
def convert_to_number(string):
    try:
        number = float(string)
        print(f"Преобразованное число: {number}")
        return number
    except ValueError:
        raise InvalidFormatError(f"Строка '{string}' не может быть преобразована в число.")
    except InvalidFormatError as e:
        print(f"Ошибка: {e}")
    finally:
        print("Завершение преобразования строки в число.")
"""TASK 9"""
def tasksCallback():
    try:
        check_positive(-5)
    except ValueError as e:
        print(e)
    try:
        check_non_empty_string("")
    except ValueError as e:
        print(e)
    check_positive_numbers(1, 2, 3, 4.5)
    check_positive_numbers(1, -2, 3)
    validate_parameters(1, 2, 3.5)
    validate_parameters(1, 0, 3)
    validate_parameters(1, 'a', 3)
    validate_positive_numbers(1, 2, 3)
    validate_positive_numbers(1, -2, 3)
    calculate_average()
    calculate_average(1, 'a', 3)
    my_list = [1, 2, 3, 4]
    remove_item_from_list(2, my_list)
    remove_item_from_list(5, "not_a_list")
    if __name__ == "__main__":
        process_numbers(1, 2, -3, "test")
        process_numbers(1, 2, 3)
    try:
        check_positive_1(-10)
    except NegativeNumberError as e:
        print(e)
    try:
        check_integer(3.14)
    except NotAnIntegerError as e:
        print(e)
    try:
        check_range(150, 1, 100)
    except ValueOutOfRangeError as e:
        print(e)
    process_values(10, 20, 150, 30)
    safe_divide(10, 0)
    safe_divide(10, 2)
    get_char_from_string("Hello", 10) 
    get_char_from_string("Hello", 1)
    convert_to_number("123abc")
    convert_to_number("456")