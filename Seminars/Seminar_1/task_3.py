import subprocess

res = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
out = res.stdout.split('\n')

if 'VERSION_CODENAME=jammy' in out and 'PRETTY_NAME="Ubuntu 22.04.1 LTS"' in out and not res.returncode:
    print('SUCCESS')
else:
    print('FAIL')
