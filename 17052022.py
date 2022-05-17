class Data:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def exist(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != "-": my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return "Все хорошо"
                else:
                    return "Неправильный год"
            else:
                return "Неправильный месяц"
        else:
            return "Неправильный день"


today = Data('13 - 5 - 2022')
print(today)
print(Data.valid(13, 5, 2022))
print(today.valid(13, 5, 2022))
print(Data.exist('13 - 5 - 2022'))
print(today.exist('13 - 5 - 2022'))


class DivisionOnZero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_on_zero(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return ("Поделить на ноль невозможно")


div = DivisionOnZero(10, 100)
print(DivisionOnZero.divide_on_zero(10, 5))
print(DivisionOnZero.divide_on_zero(10, 0.5))
print(div.divide_on_zero(100, 0))


class Error:
    def __init__(self, *args):
        self.my_list = []

        while True:
            try:
                val = int(input('Введите значение: '))
                self.my_list.append(val)
                print(f'Созданный список - {self.my_list}')
            except:
                print('Неправильное значение')