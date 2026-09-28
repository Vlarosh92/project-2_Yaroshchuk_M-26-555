def create_table(metadata: dict, table_name:str, columns:List[str]) -> dict:
    """
    Функция принимает текущие метаданные, имя таблицы и список столбцов.
    Делает проверку корректности данных и отсутствия такой таблицы,
    в случае успеха, обновляет словарь metadata и возвращает его.
    """
    try:
        #если надо создаем первый элемент
        metadata.setdefault("tables", {})
        #создаем список допустимых типов
        VALID_TYPES = {"int", "str", "bool"}
        if table_name in metadata["tables"]:
            print(f'Ошибка: Таблица "{table_name}" уже существует.')
        else:
            # Объявляем словарь хранящий данные в формате <имя:тип>
            dict_columns = dict()
            dict_columns["ID"] = "int"
            for column in columns:
                # Проверяем что разделение на имя:тип корректно
                if ":" not in column:
                    raise ValueError(f"Неверный формат колонки: '{columns}'")
                # разделяем на имя и тип
                name, dtype = column.split(":")
                # проверяем соответствие типа условию задания
                if dtype.lower() in VALID_TYPES:
                    dict_columns[name.strip()]=dtype.strip().lower()
                else:
                    print(f"Некорректное значение: <{dtype.strip()}>. Попробуйте снова.")
                    return None
            # добавляем словарь в метаданные и возвращаем

            metadata["tables"][table_name] = {name: dtype for name, dtype in dict_columns.items()}
            return metadata
    except TypeError:
        pass
    except KeyError:
        print("KeyError")

def drop_table(metadata: dict, table_name: str) -> dict:
    """
    Функция проверяет наличие таблицы в мета_данных и в случае
    успеха удаляет её
    """
    try:
        if table_name in metadata["tables"]:
            metadata["tables"].pop(table_name)
            return metadata
        else:
            print(f'Ошибка: Таблица "{table_name}" не существует.')
            return None
    except TypeError:
        pass
def list_tables(metadata: dict) -> str:
    """
    Функция возвращающая список всех таблиц
    """
    #Проверка на наличие
    metadata.setdefault("tables", {})
    return [" - " +table+"\n" for table in metadata["tables"].keys()]
