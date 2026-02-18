def filter_by_currency(transactions, currency_code):
    """
    Генератор, фильтрующий транзакции по коду валюты.

    Args:
        transactions: список словарей с транзакциями
        currency_code: код валюты для фильтрации (например, "USD")

    Yields:
        dict: транзакция с указанной валютой
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """
    Генератор, выдающий описания транзакций по очереди.

    Args:
        transactions: список словарей с транзакциями

    Yields:
        str: описание операции
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, end):
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.

    Args:
        start: начальное значение (1-9999)
        end: конечное значение (1-9999)

    Yields:
        str: номер карты в формате XXXX XXXX XXXX XXXX
    """
    for number in range(start, end + 1):
        # Форматируем как 16-значный номер с ведущими нулями
        full_number = f"{number:016d}"
        formatted = f"{full_number[:4]} {full_number[4:8]} {full_number[8:12]} {full_number[12:]}"
        yield formatted
