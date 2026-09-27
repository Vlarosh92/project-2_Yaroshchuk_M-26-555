import prompt


def welcome() -> None:
    """
    Функция ввода данных от пользователя
    """
    # Константы для цветов (чтобы код был читаемым)
    BLUE = "\033[94m"
    RESET = "\033[0m"

    print("\n\nПервая попытка запустить проект!\n")
    print("***")
    print(f"{BLUE}<command> exit{RESET} - выйти из программы")
    print(f"{BLUE}<command> help{RESET} - справочная информация")
    while True:
        user_input = prompt.string(f'Введите команду: {BLUE}')
        if user_input == "exit":
            break
        elif user_input == "help":
            print(f"{BLUE}<command> exit{RESET} - выйти из программы")
            print(f"{BLUE}<command> help{RESET} - справочная информация\n")
        else:
            continue