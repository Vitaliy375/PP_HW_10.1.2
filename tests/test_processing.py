from datetime import datetime

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def test_data() -> list[dict[str, str] | dict[str, str] | dict[str, str] | dict[str, str] | dict[str, str]]:
    """Базовые тестовые данные с state и date."""
    return [
        {"state": "EXECUTED", "date": "09/02/2026 18:49:00"},
        {"state": "PENDING", "date": "08/02/2026 12:00:00"},
        {"state": "EXECUTED", "date": "10/02/2026 10:30:00"},
        {"state": "CANCELLED", "date": "07/02/2026 15:45:00"},
        {"state": "EXECUTED", "date": "08/02/2026 20:15:00"},
    ]


class TestFilterByState:
    def test_default_executed(
        self, test_data: list[dict[str, str] | dict[str, str] | dict[str, str] | dict[str, str] | dict[str, str]]
    ) -> None:
        """Фильтр по умолчанию (EXECUTED) — 3 элемента."""
        result = filter_by_state(test_data)
        assert len(result) == 3
        assert all(item["state"] == "EXECUTED" for item in result)

    @pytest.mark.parametrize(
        "state, expected_count", [("PENDING", 1), ("CANCELLED", 1), ("EXECUTED", 3), ("NONEXISTENT", 0)]
    )
    def test_different_states(
        self,
        test_data: list[dict[str, str] | dict[str, str] | dict[str, str] | dict[str, str] | dict[str, str]],
        state: str,
        expected_count: int,
    ) -> None:
        """Фильтр по разным state."""
        result = filter_by_state(test_data, state)
        assert len(result) == expected_count

    def test_empty_list(self) -> None:
        """Пустой список."""
        result = filter_by_state([])
        assert result == []

    def test_no_state_key(self) -> None:
        """Элемент без ключа state."""
        data = [{"other": "value"}]
        result = filter_by_state(data)
        assert result == []


class TestSortByDate:
    def test_descending_default(
        self, test_data: list[dict[str, str] | dict[str, str] | dict[str, str] | dict[str, str] | dict[str, str]]
    ) -> None:
        """Сортировка по убыванию (по умолчанию)."""
        filtered = filter_by_state(test_data)
        result = sort_by_date(filtered)
        dates = [datetime.strptime(item["date"], "%d/%m/%Y %H:%M:%S") for item in result]
        assert dates == sorted(dates, reverse=True)

    def test_ascending(
        self, test_data: list[dict[str, str] | dict[str, str] | dict[str, str] | dict[str, str] | dict[str, str]]
    ) -> None:
        """Сортировка по возрастанию."""
        filtered = filter_by_state(test_data)
        result = sort_by_date(filtered, reduce=False)
        dates = [datetime.strptime(item["date"], "%d/%m/%Y %H:%M:%S") for item in result]
        assert dates == sorted(dates)

    def test_empty_list(self) -> None:
        """Пустой список."""
        result = sort_by_date([])
        assert result == []

    def test_single_item(
        self, test_data: list[dict[str, str] | dict[str, str] | dict[str, str] | dict[str, str] | dict[str, str]]
    ) -> None:
        """Один элемент."""
        result = sort_by_date([test_data[0]])
        assert result == [test_data[0]]

    def test_invalid_date_format(self) -> None:
        """Проверьте обработку неверного формата date (ожидаем ошибку или пропуск)."""
        data = [{"date": "invalid"}]
        result = sort_by_date(data)
        assert len(result) == 1
