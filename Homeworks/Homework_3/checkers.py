"""
Дополнить проект фикстурой, которая после каждого шага теста
дописывает в заранее созданный файл stat.txt строку вида:
время, кол-во файлов из конфига, размер файла из конфига,
статистика загрузки процессора из файла /proc/loadavg
(можно писать просто всё содержимое этого файла).
"""

import subprocess


def checkout(self, cmd, text):
    res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in res.stdout and res.returncode == 0:
        return True
    else:
        return False


def negative_checkout(cmd, text):
    res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    if res.returncode and (text in res.stdout or text in res.stderr):
        return True
    else:
        return False


def check_hash_crc32(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    return result.stdout


def return_stdout(cmd):
    res = (subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')).stdout
    return res
