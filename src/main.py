from components import CurrenciesList
from decorators import ConcreteDecoratorJSON, ConcreteDecoratorCSV

print('long')

def client_code(component):
    """Клиентский код работает с компонентами и декораторами через общий интерфейс"""
    print(f"RESULT:\n{component.operation()}")

if __name__ == "__main__":
    # Базовый компонент - CurrenciesList
    simple = CurrenciesList()

    print("Client: Получаем данные о валютах:")
    client_code(simple)
    print("\n")

    # Декоратор для JSON
    json_decorator = ConcreteDecoratorJSON(simple)
    print("Client: Данные в формате JSON:")
    client_code(json_decorator)
    print("\n")

    # Декоратор для CSV
    csv_decorator = ConcreteDecoratorCSV(simple)
    print("Client: Данные в формате CSV:")
    client_code(csv_decorator)
    print("\n")

    # Декораторы могут быть комбинированы:
    json_and_csv_decorator = ConcreteDecoratorCSV(json_decorator)
    print("Client: Данные в формате JSON, затем CSV:")
    client_code(json_and_csv_decorator)
