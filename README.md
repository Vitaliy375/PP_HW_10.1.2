# Учебный проект по Python

## Это приложение с дополнительными функциями работы с данными о банковских операциях пользователя.

## Цель

Цель проекта научиться программировать на реальных примерах на языке Python и и работать с Git.
Продолжаем работу над виджетом банковских операций клиента. Выкладываем свой проект на GitHub и ведем разработку по
GitFlow. Учитываем рекомендации PEP 8, продолжаем использовать линтеры и делаем атомарные коммиты.

## Инструкции по установке

В файле masks.py лежат функции маскировки номера счета и номера карты
В файле widget.py лежит функция которая выбирает из введеного: что это карта или счет и маскирует их по шаблону
и функция которая берет строку с датой и возвращает дату по шаблону
В файле progressing.py 1 функция фильтрует список словарей по ключу, а 2 функция сортирует по дате

Установка
Скопируйте функции в Python-модуль (например, utils.py в вашем проекте с Poetry).

bash

### В корне проекта (PP_HW_* или новый)

poetry add --group dev pytest # Для тестов
poetry shell
Добавьте __init__.py в папку src/ для импортов как пакета.

## Примеры

python from utils import filter_by_state, sort_by_date

### Тестовые данные (как ваши товары + state/date)

transactions = [
{"state": "EXECUTED", "date": "2026-01-29T10:00:00", "desc": "Перевод"},
{"state": "PENDING", "date": "2026-01-28T15:30:00", "desc": "Ожидание"},
{"state": "EXECUTED", "date": "2026-01-27T09:15:00", "desc": "Платеж"},
{"state": "EXECUTED", "date": "2026-01-29T12:00:00", "desc": "Снятие"}
]

### Фильтр по умолчанию (EXECUTED)

executed = filter_by_state(transactions)
print(executed)  # 1-й и 4-й элементы[cite:1]

### Сортировка по убыванию даты (новые сверху)

sorted_tx = sort_by_date(executed)
print([tx["desc"] for tx in sorted_tx])  # ['Снятие', 'Перевод']
Запуск: python -m src.main (не python src/main.py).

Комбинированное использование Фильтр + сортировка в цепочке:

### Только EXECUTED, отсортированные по дате (возрастание)

recent_first = sort_by_date(filter_by_state(transactions, "EXECUTED"), reverse=False)
print(recent_first[0]["date"])  # Самая новая дата
Интеграция с вашими прошлыми функциями (товары + транзакции).

## Тестирование
Проект покрыт юнит-тестами с использованием pytest (покрытие ~98%). Тесты проверяют основные функции обработки данных,
валидацию входных параметров и обработку ошибок.

Запуск тестов bash

### Установка зависимостей для тестов

pip install -r requirements-test.txt

### Запуск всех тестов

pytest

### Запуск с покрытием

pytest --cov=src --cov-report=html

### Запуск конкретного модуля

pytest tests/test_data_processor.py -v

### Тесты с фикстурой (например, для БД)

pytest tests/integration/ -m integration


## Модуль generators
Содержит генераторы для эффективной обработки данных:

### filter_by_currency(transactions, currency_code)
Фильтрует транзакции по коду валюты, возвращает итератор.

python
usd_transactions = filter_by_currency(transactions, "USD")
for trans in usd_transactions:
    print(trans['description'])
transaction_descriptions(transactions)
Возвращает генератор описаний транзакций.

python descriptions = transaction_descriptions(transactions)
for desc in descriptions:
    print(desc)
card_number_generator(start, end)
Генерирует номера карт в формате XXXX XXXX XXXX XXXX.

python for card in card_number_generator(1, 5):
    print(card)
        0000 0000 0000 0001
        0000 0000 0000 0002
        ... text

## Покрытие тестами

Тесты обеспечивают > 90 % покрытия:
- Все ветки логики генераторов протестированы
- Обработаны edge - кейсы(пустые списки, отсутствующие ключи)
- Параметризация для множественных проверок
- Фикстура `sample_transactions` для переиспользования данных

Запуск: `pytest test_generators.py - -cov = generators - -cov - report = term - missing`
