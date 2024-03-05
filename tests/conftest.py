import datetime

import pytest
from test1 import checkout
import random
import string
import yaml

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
        if checkout(f"cd {data['FOLDER_IN']}; dd if=dev/urandom of={filename} bs={data['size']} count=1 iflag=fullblock".format(data["FOLDER_IN"], filename),
                    ""):
            list_of_files.append(filename)
    return list_of_files


@pytest.fixture()
def make_subfolder():
    test_file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfolder_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not checkout("cd {}; mkdir {}".format(data["FOLDER_IN"], subfolder_name), ""):
        return None, None
    if not checkout(
            f"cd {data['FOLDER_IN']}/{subfolder_name}; dd if=dev/urandom of={test_file_name} bs={data['size']} count=1 iflag=fullblock".format(data["FOLDER_IN"], subfolder_name, \
                                                                                     test_file_name), ""):
        return subfolder_name, None
    else:
        return subfolder_name, test_file_name





@pytest.fixture(autouse=True)
def print_time():
    print("start: {}".format(datetime.now().strftime("%H:%M:%S.%f")))
    yield
    print("stop: {}".format(datetime.now().strftime("%H:%M:%S.%f")))


@pytest.fixture()
def make_bad_file():
    if checkout(f"cd {data['FOLDER_IN']}; 7z a {data['FOLDER_OUT']}/arx2_bad.7z", "") and \
            checkout(f"truncate -s 1 {data['FOLDER_OUT']}/arx2_bad.7z", ""):
        return "arx2_bad"
    return None
