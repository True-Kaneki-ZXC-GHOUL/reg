"""
Модуль форматирования регистра текста.

Преобразует текст в верхний, нижний регистр или формат с заглавных букв.
"""


def format_case(text: str, mode: str) -> str:
    """
    Преобразует текст в указанный регистр.

    Параметры:
        text (str): Исходный текст для преобразования.
        mode (str): Режим форматирования. Может принимать значения:
            - 'upper' — преобразование в ВЕРХНИЙ РЕГИСТР
            - 'lower' — преобразование в нижний регистр
            - 'title' — преобразование в Заглавные Буквы Каждого Слова

    Возвращает:
        str: Преобразованный текст.

    Исключения:
        ValueError: Если mode не является одним из допустимых значений.
        TypeError: Если text или mode имеют неправильный тип.

    Примеры:
        >>> format_case("Hello World", "upper")
        'HELLO WORLD'
        >>> format_case("Hello World", "lower")
        'hello world'
        >>> format_case("hello world", "title")
        'Hello World'
    """

    # Проверка типа входных данных
    if not isinstance(text, str):
        raise TypeError(f"Параметр 'text' должен быть строкой, получен {type(text).__name__}")
    
    if not isinstance(mode, str):
        raise TypeError(f"Параметр 'mode' должен быть строкой, получен {type(mode).__name__}")

    # Проверка допустимых режимов
    valid_modes = ('upper', 'lower', 'title')
    if mode not in valid_modes:
        raise ValueError(
            f"Недопустимый режим '{mode}'. "
            f"Допустимые режимы: {', '.join(valid_modes)}"
        )

    # Обработка пустого текста (пустая строка — валидный случай)
    if text == "":
        return ""

    # Применение соответствующего преобразования
    if mode == 'upper':
        return text.upper()
    elif mode == 'lower':
        return text.lower()
    else:  # mode == 'title'
        return text.title()


# Блок для самостоятельного тестирования модуля
if __name__ == "__main__":
    # Демонстрация работы модуля
    test_texts = [
        "Привет, мир!",
        "python ПРОГРАММИРОВАНИЕ",
        "hello WORLD",
        "",
        "   пробелы в начале и конце   "
    ]
    
    print("=" * 60)
    print("Тестирование модуля форматирования регистра")
    print("=" * 60)
    
    for text in test_texts:
        print(f"\nИсходный текст: '{text}'")
        print(f"  upper: '{format_case(text, 'upper')}'")
        print(f"  lower: '{format_case(text, 'lower')}'")
        print(f"  title: '{format_case(text, 'title')}'")
        print("-" * 40)
    
    # Тестирование обработки ошибок
    print("\nТестирование обработки ошибок:")
    try:
        format_case("test", "invalid_mode")
    except ValueError as e:
        print(f"  ✓ ValueError: {e}")
    
    try:
        format_case(123, "upper")  # type: ignore
    except TypeError as e:
        print(f"  ✓ TypeError: {e}")
    
    try:
        format_case("test", 456)  # type: ignore
    except TypeError as e:
        print(f"  ✓ TypeError: {e}")
    
    print("\n" + "=" * 60)
    print("Все тесты пройдены!")