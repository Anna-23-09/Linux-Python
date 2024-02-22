"""
Написать автотест на bash, который читает содержимое файла
/etc/os-release (в нем хранится информация о версии системы)
и выведет на экран “SUCCESS” если в нем содержатся версия
22.04.1, кодовое имя jammy и команда чтения файла выполнена
без ошибок. В противном случае должно выводится “FAIL”.
"""

import subprocess

res = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
if 'jammy' in res.stdout and '22.04.1' in res.stdout and not res.returncode:
    print('SUCCESS')
else:
    print('FAIL')
