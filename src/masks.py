def get_mask_card_number(number: str) -> str:
    """
    Преобразование числа в маску.

    :param number: str принимает целочисленный вид данных
    :return: str возвращает строку в формате XXXX XX** **** XXXX
    """
    res_fin = []
    conv_str = str(number)
    count_stars = len(conv_str[6:-4]) * "*"
    join_number = f"{conv_str[:6]}{count_stars}{conv_str[-4:]}"
    for i in range(0, len(join_number), 4):
        res_fin.append(join_number[i: i + 4])
    return " ".join(res_fin)


def get_mask_account(number: str) -> str:
    """
    Преобразование числа в маску счета.

    :param number: str Принимает целочисленный вид данных
    :return: str возвращает строку в формате **XXXX
    """
    conv_str = str(number)
    return f"**{conv_str[-4:]}"



