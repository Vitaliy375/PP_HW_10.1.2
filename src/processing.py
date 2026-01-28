def filter_by_state(list_state: list[dict],state: str ="EXECUTED")-> [list]:
    """Функция, которая принимает список словарей и опционально значение для ключа
    state(по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий
    только те словари, у которых ключ state соответствует указанному значению."""
    filter_list = []
    for x in list_state:
        if x["state"] == state:
            filter_list.append(x)
    return filter_list


def sort_by_date(list_dict: list[dict], reduce: bool =True) -> [list]:
    """Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание) и возвращает новый список, отсортированный по дате"""
    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=reduce)
    return sorted_list
