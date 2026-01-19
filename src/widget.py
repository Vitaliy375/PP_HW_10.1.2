from src.masks import get_mask_card_number
from src.masks import get_mask_account


def parse_and_mask(card_string):
    """Функция из строки с типом и номером, маскирует номер карты или счета."""
    parts = card_string.rsplit(' ', 1)
    if len(parts) != 2:
        return card_string
    name, number = parts
    if 'Счет' in name:
        return name + " " + get_mask_account(number)  # Маскировка счета
    else:
        clean_num = number.replace(' ', '')
        if len(clean_num) == 16:
            clean_num = number.replace(' ', '')
            return name + " " + get_mask_card_number(clean_num)
        return card_string


#def get_date(str: "") -> str:
 #   pass

#return f"{'ДД.ММ.ГГГГ'}"



if __name__ == "__main__":
    card_string = "Счет 73654108430135874305"
    print(parse_and_mask(card_string))
 
