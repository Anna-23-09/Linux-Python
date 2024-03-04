"""
Установить пакет для расчёта crc32
sudo apt install libarchive-zip-perl
• Доработать проект, добавив тест команды расчёта хеша (h). Проверить, что хеш совпадает с рассчитанным командой crc32.
"""

import subprocess
from test1.py import checkout

FOLDER_IN = "home/user/tst"
FOLDER_OUT = "home/user/out"
FOLDER_EXTRACT = "/home/user/folder1"
FOLDER_EXTRACT_2 = "/home/user/folder2"

def test_step_10():
    #test10
    res = subprocess.run("crc32 /home/user/out/arx2.7z", shell=True, stdout=subprocess.PIPE, encoding='UTF-8')
    assert checkout(f"cd {FOLDER_OUT}; 7z h arx2.7z", f"{(res.stdout).rstrip().lower()}"), "test10 FAIL"
