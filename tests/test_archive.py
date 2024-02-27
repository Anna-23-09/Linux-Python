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
    res1 = checkout(f"cd {FOLDER_IN}; 7z a {FOLDER_OUT}/arx2", "Everything is OK")
    res2 = checkout(f"ls {FOLDER_OUT}", "arx2.7z")
    assert res1 and res2, "test1 FAIL"


def test_step_2():
    # test1
    res1 = checkout(f"cd {FOLDER_OUT}; 7z e arx2.7z -o{FOLDER_EXTRACT} -y", "Everything is OK")
    res2 = checkout(f"ls {FOLDER_EXTRACT}", "arx2.7z")
    assert res1 and res2, "test2 FAIL"
