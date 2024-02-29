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
    return checkout("mkdir {} {} {} {}".format(data["FOLDER_IN"], data["FOLDER_OUT"], data["FOLDER_EXTRACT"], data["FOLDER_EXTRACT_2"]), "")


@pytest.fixture()
def clear_folders():
    return checkout("rm -rf {}/* {}/* {}/* {}/*".format(data["FOLDER_IN"], data["FOLDER_OUT"], data["FOLDER_EXTRACT"], data["FOLDER_EXTRACT_2"]), "")


@pytest.fixture()
def make_files():
    list_of_files = []
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout("cd {}; dd if=dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data["FOLDER_IN"], filename), ""):
            list_of_files.append(filename)
    return list_of_files


@pytest.fixture()
def make_subfolder():
    test_file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfolder_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not checkout("cd {}; mkdir {}".format(data["FOLDER_IN"], subfolder_name), ""):
        return None, None
    if not checkout("cd {}/{}; dd if=dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data["FOLDER_IN"], subfolder_name,
                                                                                             test_file_name), ""):
        return subfolder_name, None
    else:
        return subfolder_name, test_file_name


@pytest.fixture(autouse=True)
def print_time():
    print("start: {}".format(datetime.now().strftime("%H:%M:%S.%f")))
    yield
    print("stop: {}".format(datetime.now().strftime("%H:%M:%S.%f")))
