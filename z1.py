#  1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
#  В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
#  Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, vyrabotka_hours, stavka_per_hour, premiya = argv

res = float(vyrabotka_hours) * float(stavka_per_hour) + float(premiya)
print("ЗП составит: ", res)
