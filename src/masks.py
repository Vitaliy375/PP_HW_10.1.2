def get_mask_card_number(number: int) -> str:
    """
    Преобразование числа в маску.

    :param number: int принимает целочисленный вид данных
    :return: str возвращает строку в формате XXXX XX** **** XXXX
    """
    if number < 0 or not isinstance(number, int):
        raise ValueError("Неверный номер карты")
    conv_str = str(number)
    if len(conv_str) < 10:
        raise ValueError("Номер карты слишком короткий")
    if number < 0: raise ValueError("Номер не может быть отрицательным")
    res_fin = []
    count_stars = len(conv_str[6:-4]) * "*"
    join_number = f"{conv_str[:6]}{count_stars}{conv_str[-4:]}"
    for i in range(0, len(join_number), 4):
        res_fin.append(join_number[i: i + 4])
    return " ".join(res_fin)


def get_mask_account(number: int) -> str:
    """
    Преобразование числа в маску счета.

    :param number: int Принимает целочисленный вид данных
    :return: str возвращает строку в формате **XXXX
    """
    conv_str = str(number)
    return f"**{conv_str[-4:]}"



