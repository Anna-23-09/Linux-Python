"""
Написать функцию на Python, которой передаются в качестве параметров команда и текст.
Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False в противном случае.
Передаваться должна только одна строка, разбиение вывода использовать не нужно.
"""

import subprocess


def simple_def(command: str, text: str):    # Принимаем на вход команду и текст, который будем искать в выводе команды
    res = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = res.stdout.lower()    # вывод команды помещаем в переменную out

    if text in out and not res.returncode:  # проверяем, есть ли text в выводе команды (out) и что вывод != не 0
        return True
    else:
        return False


a = "cat /etc/os-release"   # команда
b = "url"   # такая строка в выводе есть, ожидаем True
c = "cat"   # такой строки нет, ожидаем False
print(simple_def(a, b))
print(simple_def(a, c))
