import pytest
from src.components import CurrenciesList
from src.decorators import ConcreteDecoratorJSON, ConcreteDecoratorCSV

def test_currencies_list():
    component = CurrenciesList()
    result = component.operation()
    assert isinstance(result, dict)
    assert "USD" in result

def test_json_decorator():
    component = CurrenciesList()
    decorator = ConcreteDecoratorJSON(component)
    result = decorator.operation()
    assert result.startswith("{") and result.endswith("}")

def test_csv_decorator():
    component = CurrenciesList()
    decorator = ConcreteDecoratorCSV(component)
    result = decorator.operation()
    assert "Currency,Rate" in result
    assert "USD" in result
