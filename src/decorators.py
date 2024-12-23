import json
import csv
from io import StringIO
from components import Component

class Decorator(Component):
    """Базовый декоратор"""
    def __init__(self, component: Component):
        self._component = component

    def operation(self):
        return self._component.operation()

class ConcreteDecoratorJSON(Decorator):
    """Декоратор для преобразования данных в формат JSON"""
    def operation(self):
        data = self._component.operation()  # Получаем данные от компонента
        return json.dumps(data, indent=4)

class ConcreteDecoratorCSV(Decorator):
    """Декоратор для преобразования данных в формат CSV"""
    def operation(self):
        data = self._component.operation()
        # Если данные в формате JSON (строка), преобразуем обратно в словарь
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                raise ValueError("Input data must be a dictionary or a valid JSON string.")

        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(["Currency", "Rate"])  # Заголовок
        for currency, rate in data.items():
            writer.writerow([currency, rate])
        return output.getvalue()
