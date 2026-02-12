import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "number, expected",
    [
        (1234567890123456, "1234 56** **** 3456"),  # 16 цифр
        (1234567890123456789, "123456 ***** 6789"),  # 19 цифр
        (1234567890, "1234 5678 90"),               # 10 цифр (минимум)
        (9999999999999999, "9999 99** **** 9999"),   # Все 9
    ]
)
def test_get_mask_card_number_valid(number: int, expected: str):
    """Проверяет валидные номера карт разной длины."""
    assert get_mask_card_number(number) == expected

def test_get_mask_card_number_negative():
    """Отрицательное число для карты."""
    with pytest.raises(IndexError):
        get_mask_card_number(-1234567890123456)

def test_get_mask_card_number_too_short():
    """Слишком короткий номер (менее 10 цифр)."""
    with pytest.raises(IndexError):
        get_mask_card_number(12345)

## Тесты для get_mask_account
@pytest.mark.parametrize(
    "number, expected",
    [
        (12345678, "**5678"),
        (123, "**0123"),      # Менее 4 цифр
        (73654108430135874305, "**4305"),  # Длинный счет
    ]
)
def test_get_mask_account_valid(number: int, expected: str):
    """Проверяет валидные счета разной длины."""
    assert get_mask_account(number) == expected

def test_get_mask_account_negative():
    """Отрицательный счет."""
    assert get_mask_account(-12345678) == "**5678"  # str(-n) работает, последние 4

if __name__ == "__main__":
    pytest.main([__file__, "-v"])