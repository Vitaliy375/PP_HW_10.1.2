import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


#TestFilterByCurrency:
def test_filters_usd_transactions(self, sample_transactions):
    usd_gen = filter_by_currency(sample_transactions, "USD")
    usd_transactions = list(usd_gen)
    assert len(usd_transactions) == 3
    assert usd_transactions[0]["id"] == 939719570

def test_no_matching_currency(self, sample_transactions):
    rub_gen = filter_by_currency(sample_transactions, "EUR")
    assert list(rub_gen) == []

def test_empty_list(self):
    empty_gen = filter_by_currency([], "USD")
    assert list(empty_gen) == []

def test_missing_operationAmount(self):
    transaction = [{"id": 1, "description": "test"}]
    gen = filter_by_currency(transaction, "USD")
    assert list(gen) == []


# TestTransactionDescriptions:
@pytest.mark.parametrize("desc_index, expected_desc", [
    (0, "Перевод организации"),
    (1, "Перевод со счета на счет"),
    (2, "Перевод со счета на счет"),
    (3, "Перевод с карты на карту")
])
def test_correct_descriptions(self, sample_transactions, desc_index, expected_desc):
    gen = transaction_descriptions(sample_transactions)
    descriptions = list(gen)
    assert descriptions[desc_index] == expected_desc

def test_empty_list(self):
    gen = transaction_descriptions([])
    assert list(gen) == []

def test_single_transaction(self):
    single = [{"description": "Тест"}]
    gen = transaction_descriptions(single)
    assert list(gen) == ["Тест"]


#TestCardNumberGenerator:
def test_small_range(self):
    numbers = list(card_number_generator(1, 5))
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]
    assert numbers == expected

def test_formatting(self):
    numbers = list(card_number_generator(1000, 1001))
    assert numbers[0] == "0000 0000 0000 1000"

def test_end_value_inclusive(self):
    numbers = list(card_number_generator(1, 1))
    assert numbers == ["0000 0000 0000 0001"]

def test_large_range(self):
    numbers = list(card_number_generator(9999999999999998, 9999999999999999))
    assert numbers[0] == "9999 9999 9999 9998"

def test_start_greater_than_end(self):
    numbers = list(card_number_generator(10, 5))
    assert numbers == []
