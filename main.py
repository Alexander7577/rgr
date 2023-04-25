from bs4 import BeautifulSoup
import requests


class ConversionException(Exception):
    pass


class Converter:
    @staticmethod
    def convert(number: str, from_system: str, to_system: str):
        if not number.isdigit() or int(from_system) < 2 or int(to_system) < 2:
            raise ConversionException("Не удалось обработать данные!")

        url = f'https://numsys.ru/convert/{number}/{from_system}/{to_system}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        nums = soup.find_all('app-formatted-number')
        result = nums[1].find_all(class_="ng-star-inserted")
        n = ''.join(n.text for n in result)

        return n


def greating():
    print("=====================")
    print("     Калькулятор      ")
    print("  систем счисления    ")
    print("======================")
    print(" формат ввода: x y z  ")
    print("  x - первое значение ")
    print("  y - второе значение ")
    print("   z - вид операции   ")
    print("======================")
    print()


greating()
data = input().split()
try:
    if len(data) != 3:
        raise ConversionException("Неправильный формат ввода!")
    number, from_system, to_system = data
    result = Converter.convert(number, from_system, to_system)
    print(result)
except ConversionException as e:
    print(f"Ошибка пользователя, \n{e}")
except Exception:
    print(f"не удаётся обработать запрос, попробуйте позже=(")
