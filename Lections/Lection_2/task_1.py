import subprocess

result_1 = subprocess.run(['ping', '-c', '3', '-n', 'yandex.ru'], encoding='utf-8', stdout=subprocess.DEVNULL)
print(result_1.stdout)

result_2 = subprocess.run(['ping', '-c', '3', '-n', 'yandex.ru'], encoding='utf-8', stdout=subprocess.PIPE)
print(result_2.stdout)

result_3 = subprocess.run(['ping', '-c', '3', '-n', 'host.host'], encoding='utf-8', stderr=subprocess.STDOUT,
                          stdout=subprocess.PIPE)
print(result_3.stdout)
