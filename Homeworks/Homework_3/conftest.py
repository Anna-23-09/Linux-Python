from datetime import datetime
import pytest
import random
import string
import yaml
from checkers import checkout, return_stdout

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folders():
    return checkout("mkdir {} {} {} {}".format(data["FOLDER_IN"], data["FOLDER_OUT"], data["FOLDER_EXTRACT"],
                                               data["FOLDER_EXTRACT_2"]), "")


@pytest.fixture()
def clear_folders():
    return checkout("rm -rf {}/* {}/* {}/* {}/*".format(data["FOLDER_IN"], data["FOLDER_OUT"], data["FOLDER_EXTRACT"],
                                                        data["FOLDER_EXTRACT_2"]), "")


@pytest.fixture()
def make_files():
    list_of_files = []
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout(f"cd {data['FOLDER_IN']}; dd if=dev/urandom of={filename} bs={data['size']} count=1 iflag=fullblock", ''):
            list_of_files.append(filename)
    return list_of_files


@pytest.fixture()
def make_subfolder():
    test_file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfolder_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not checkout("cd {}; mkdir {}".format(data["FOLDER_IN"], subfolder_name), ""):
        return None, None
    if not checkout(f"cd {data['FOLDER_IN']}/{subfolder_name}; "
        f"dd if=dev/urandom of={test_file_name} bs={data['size']} count=1 iflag=fullblock", ""):
        return subfolder_name, None
    else:
        return subfolder_name, test_file_name


@pytest.fixture()
def create_bad_archive():
    checkout(f"cd {data['FOLDER_IN']}; 7z a -t{data['ARC_TYPE']} {data['FOLDER_OUT']}/arx2", "Everything is OK")
    checkout(f"cp {data['FOLDER_OUT']}/arx2.{data['ARC_TYPE']} {data['FOLDER_BAD']}", "")
    checkout(f"truncate -s 1 {data['FOLDER_BAD']}/arx2.{data['ARC_TYPE']}", "")


@pytest.fixture(autouse=True)
def print_time():
    print("start: {}".format(datetime.now().strftime("%H:%M:%S.%f")))
    yield
    print("stop: {}".format(datetime.now().strftime("%H:%M:%S.%f")))


@pytest.fixture(autouse=True)
def stat_fixture():
    pass
    yield
    time_stamp = datetime.now().strftime("%H:%M:%S.%f")
    files_count = data["count"]
    file_size = data["bs"]
    cpu_stat = return_stdout("cat /proc/loadavg")
    checkout(f'cd {data["stat_file_dir"]}; echo "time = {time_stamp}, files_count = {files_count}, file_size = {file_size}, cpu_stat = {cpu_stat}" >> stat.txt','')
