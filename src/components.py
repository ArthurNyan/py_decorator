class Component:
    """Базовый интерфейс для компонента"""
    def operation(self):
        pass

class CurrenciesList(Component):
    """Конкретный компонент для получения списка валют (в виде словаря)"""
    def operation(self):
        # Пример словаря с курсами валют
        return {
            "USD": 75.5,
            "EUR": 82.2,
            "GBP": 94.3,
        }
