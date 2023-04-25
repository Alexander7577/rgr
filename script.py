from bs4 import BeautifulSoup
import requests


class ConversionException(Exception):
    pass


class Converter:
    @staticmethod
    def convert(first_Value: str, type_of_operation: str, second_value: str, system: str):
        if not first_Value.isdigit():
            raise ConversionException("значение указано некорректно!")
        if type_of_operation != "add" and type_of_operation != "subtract" and type_of_operation and "multiply" and type_of_operation != "divide":
            raise ConversionException("Тип операции указан некорректно!")
        if not second_value.isdigit():
            raise ConversionException("Второе значение указано некорректно!")
        if int(system) < 2:
            raise ConversionException("Система счисления указана некорректно!")

        for i in first_Value:
            if int(i) >= int(system):
                raise ConversionException(f"{i} не может использоваться в этой системе счисления!")

        for i in second_value:
            if int(i) >= int(system):
                raise ConversionException(f"{i} не может использоваться в этой системе счисления!")

        url = f'https://numsys.ru/calculate/{first_Value}/{type_of_operation}/{second_value}/{system}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        nums = soup.find_all('app-formatted-number')
        result = nums[-1].find_all(class_="ng-star-inserted")
        n = ''.join(n.text for n in result)

        return n


class Operations:
    @staticmethod
    def greating():
        print("==========================")
        print("       Калькулятор        ")
        print("     систем счисления     ")
        print("==========================")
        print("   формат ввода: x y z w  ")
        print("    x - первое значение   ")
        print("     y - вид операции     ")
        print("    z - второе значение   ")
        print("   w - система счисления  ")
        print("==========================")
        print()

    @staticmethod
    def fix_operation(type):
        if type == "+":
            type = "add"
        if type == "-":
            type = "subtract"
        if type == "*":
            type = "multiply"
        if type == "/":
            type = "divide"

        return type


Operations.greating()
data = input().split()
try:
    if len(data) != 4:
        raise ConversionException("Неправильный формат ввода!")
    first_Value, type_of_operation, second_value, system = data
    type_of_operation = Operations.fix_operation(type_of_operation)

    result = Converter.convert(first_Value, type_of_operation, second_value, system)
    print(result)
except ConversionException as e:
    print(f"Ошибка пользователя, \n{e}")
except Exception:
    print(f"не удаётся обработать запрос, попробуйте позже=(")
