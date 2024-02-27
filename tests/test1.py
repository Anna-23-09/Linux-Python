import subprocess

FOLDER_IN = "home/user/tst"
FOLDER_OUT = "home/user/out"
FOLDER_EXTRACT = "/home/user/folder1"

def checkout(cmd, text):
    res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in res.stdout and res.returncode == 0:
        return True
    else:
        return False


def test_step_1():
    # test1
    assert checkout(f"cd {FOLDER_IN}; 7z a ../out/arx2", "Everything is OK"), "test1 Fail"


def test_step_2():
    # test2
    assert checkout(f"cd {FOLDER_OUT}; 7z e .arx2.7z -o{FOLDER_EXTRACT} -y", "Everything is OK"), "test2 Fail"


def test_step_3():
    # test3
    assert checkout(f"cd {FOLDER_OUT}; 7z t .arx2.7z", "Everything is OK"), "test3 Fail"


def test_step_4():
    # test4
    assert checkout(f"cd {FOLDER_OUT}; 7z d .arx2.7z", "Everything is OK"), "test4 Fail"


def test_step_5():
    # test5
    assert checkout(f"cd {FOLDER_OUT}; 7z u .arx2.7z", "Everything is OK"), "test5 Fail"


