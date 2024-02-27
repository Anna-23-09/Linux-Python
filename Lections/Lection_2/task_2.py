import subprocess


def checkout(cmd, text):
    res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in res.stdout and res.returncode == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    # test1
    if checkout("cd home/zerg/tst; 7z a ../out/arx2", "Everything is OK"):
        print("test1 Fail")

    # test2
    assert checkout("cd home/zerg/out; 7z e .arx2.7z -o/home/zerg/folder1 -y", "Everything is OK"), print("test2 Fail")
    # тоже проверка, как и test1, но вывода не будет, плюс запись короче
    # test3
    if checkout("cd home/zerg/out; 7z t .arx2.7z", "Everything is OK"):
        print("test3 Success")
    else:
        print("test3 Fail")
