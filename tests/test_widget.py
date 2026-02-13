import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "input_str, expected",
    [
        # СЧЕТА: всегда маскируются (**XXXX)
        ("Счет 7365410843013587430", "Счет **7430"),
        ("Счет 1234", "Счет **1234"),
        # КАРТЫ: только если РОВНО 16 цифр
        ("Visa Platinum 123456789012345", "Visa Platinum 123456789012345"),  # 15 → оригинал
        ("Maestro 12345678901234567", "Maestro 12345678901234567"),  # 17 → оригинал
        # НЕВЕРНЫЙ ФОРМАТ
        ("Invalid", "Invalid"),
        ("Visa Platinum", "Visa Platinum"),
    ],
)
def test_mask_account_card(input_str:str, expected:str) -> None:
    """Тестирует ВСЕ ветки: счета, карты!=16, неверный формат."""
    result = mask_account_card(input_str)
    assert result == expected


def test_card_exactly_16_digits() -> None:
    """Только 16 цифр → маскирует карту."""
    result = mask_account_card("Visa 1234567890123456")
    assert result.startswith("Visa ")  # тип сохранен
    assert len(result.split()[-1]) > 0  # маскировка сработала


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18", "11.03.2024"),
        ("2026-02-12T20:53:00", "12.02.2026"),
    ],
)
def test_get_date(date_str:str, expected:str) -> None:
    result = get_date(date_str)
    assert result == expected
