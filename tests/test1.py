import subprocess


def checkout(cmd, text):
    res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in res.stdout and res.returncode == 0:
        return True
    else:
        return False


def test_step_1():
    # test1
    assert checkout("cd home/zerg/tst; 7z a ../out/arx2", "Everything is OK"), "test1 Fail"


def test_step_2():
    # test2
    assert checkout("cd home/zerg/out; 7z e .arx2.7z -o/home/zerg/folder1 -y", "Everything is OK"), "test2 Fail"


def test_step_3():
    # test3
    assert checkout("cd home/zerg/out; 7z t .arx2.7z", "Everything is OK"), "test3 Fail"
