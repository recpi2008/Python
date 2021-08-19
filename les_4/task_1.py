"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы
сотрудника. В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
 Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, work_hour, salary_hour, prize = argv
script_name = int(script_name)
work_hour = int(work_hour)
prize = int(prize)
salary_user = (work_hour * salary_hour) + prize
print(f"заработная плата сотрудника {salary_user}")