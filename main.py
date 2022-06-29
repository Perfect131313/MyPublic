from decimal import Decimal

def num_format(num_x): # числовой формат:
    n = Decimal(str(num_x))
    number = n.quantize(Decimal("1.00"))  # "1.00" - здесь задаём кол-во знаков после запятой
    formi = '{0:,}'.format(number).replace(',', ' ')  # (',', ' ') - во вторых кавычках ставим нужный разделитель
    return formi