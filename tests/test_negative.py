"""
Создать отдельный файл для негативных тестов. Функцию
проверки вынести в отдельную библиотеку. Повредить архив
(например, отредактировав его в текстовом редакторе).
Написать негативные тесты работы архиватора с командами
распаковки (e) и проверки (t) поврежденного архива.
"""

import subprocess

FOLDER_IN = "home/user/tst"
FOLDER_OUT = "home/user/out"
FOLDER_EXTRACT = "-o/home/zerg/folder1"


def negative_checkout(cmd, text):
    res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    if res.returncode and (text in res.stdout or text in res.stderr):
        return True
    else:
        return False


def test_negative_step_1():
    # test2
    assert negative_checkout(f"cd {FOLDER_OUT}; 7z e .arx2_bad.7z {FOLDER_EXTRACT} -y", "ERROR"), "test2 Fail"


def test_negative_step_2():
    # test2
    assert negative_checkout(f"cd {FOLDER_OUT}; 7z t .arx2_bad.7z {FOLDER_EXTRACT} -y", "ERROR"), "test2 Fail"


