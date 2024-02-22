"""
Написать функцию на Python, которой передаются в качестве параметров команда и текст.
Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False в противном случае.
Передаваться должна только одна строка, разбиение вывода использовать не нужно.
"""

import subprocess


def simple_def(command: str, text: str):
    res = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = res.stdout.lower()

    if text in out and not res.returncode:
        return True
    else:
        return False


a = "cat /etc/os-release"
b = "url"
c = "cat"
print(simple_def(a, b))
print(simple_def(a, c))
