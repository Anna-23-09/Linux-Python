import subprocess


def checkout(self, cmd, text):
    res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in res.stdout and res.returncode == 0:
        return True
    else:
        return False


def getout(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    return result.stdout.upper()


def negative_checkout(cmd, text):
    res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    if res.returncode and (text in res.stdout or text in res.stderr):
        return True
    else:
        return False


