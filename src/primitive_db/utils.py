import json


def load_metadata(filepath: str) -> dict:
    """
    Функция загружает метаданные из файла filepath
    если прочесть не получается возращает пустой словарь
    """
    try :
        with open(filepath) as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}

def save_metadata(filepath: str, data: dict) -> None:
    """
    Сохраняет переданные метаданные в файл filepath
    """
    try :
        with open(filepath, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)
    except PermissionError:
        pass
    except FileNotFoundError:
        pass