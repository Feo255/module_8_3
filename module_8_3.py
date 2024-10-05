class Car:
    def __init__(self, model, _vin, number):
        self.model = model
        vv = self.__is_valid_vin(_vin)
        if vv is True:
            self._vin = _vin
        vn = self.__is_valid_number(number)
        if vn is True:
            self.number = number

    def __is_valid_vin(self, _vin):
        valid_vin = False
        
        if type(_vin) != int:
            raise IncorrectVinNumber('Некорректный тип vin номер')

        if _vin >= 1000000 and _vin <= 9999999:

            valid_vin = True
            return valid_vin

        else:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

    def __is_valid_number(self, number):
        valid_number = False
        if type(number) != str:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(number) !=6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            valid_number = True
            return valid_number


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message



class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message



try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
