import prompt
import shlex
from .core import create_table, drop_table


def print_help() -> None:
    """Выдает информацию в консоль на вызов команды help"""
    # Константы для цветов
    blue = "\033[94m"
    reset = "\033[0m"

    print(f"\n{reset}***Процесс работы с таблицей***")
    print("Функции:")
    print(f"<{blue}command{reset}> create_table <имя_таблицы> <столбец1:тип> .. - создать таблицу")
    print(f"<{blue}command{reset}> list_tables - показать список всех таблиц")
    print(f"<{blue}command{reset}> drop_table <имя_таблицы> - удалить таблицу")

    print("\nОбщие команды:")
    print(f"<{blue}command{reset}> {blue}exit{reset} - выход из программы")
    print(f"<{blue}command{reset}> {blue}help{reset} - справочная информация\n")

def run() -> None:
    """
    Функция ввода данных от пользователя
    """
    # Константы для цветов
    blue = "\033[94m"
    reset = "\033[0m"

    print("\n***Процесс работы с таблицей***\n")
    print("Функции:\n")
    print(f"<{blue}command{reset}> create_table <имя_таблицы> <столбец1:тип> <столбец2:тип> .. - создать таблицу")
    print(f"<{blue}command{reset}> list_tables - показать список всех таблиц")
    print(f"<{blue}command{reset}> drop_table <имя_таблицы> - удалить таблицу")
    print(f"<{blue}command{reset}> {blue}exit{reset} - выход из программы")
    print(f"<{blue}command{reset}> {blue}help{reset} - справочная информация ")
    while True:


        user_input = prompt.string(f'>>>Введите команду: ')

        args = shlex.split(user_input)
        match args[0]:
            case "exit":
                break
            case "help":
                print_help()
            case "create_table":
                result = create_table(meta, args[1], [col for col in args[2:]])
                if not result is None:
                    pass
                    #save_metadata(filepath, result)
            case "list_tables":
                pass
            case "drop_table":
                result = drop_table(meta, args[1])
                if not result is None:
                    pass
                    # save_metadata(filepath, result)
            case _:
                print(f"{reset}Функции <{user_input}> нет. Попробуйте снова.")

