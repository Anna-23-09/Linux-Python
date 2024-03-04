"""
Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).
"""


from test1.py import checkout

FOLDER_IN = "home/user/tst"
FOLDER_OUT = "home/user/out"
FOLDER_EXTRACT = "/home/user/folder1"
FOLDER_EXTRACT_2 = "/home/user/folder2"

def test_step_8():
    #test8
    assert checkout(f"cd {FOLDER_OUT}; 7z l arx2.7z", "2 files")

def test_step_9():
    #test9
    assert checkout(f"cd {FOLDER_OUT}; 7z x arx2.7z -o{FOLDER_EXTRACT_2} -y", "Everything is OK"), "test9 FAIL"

