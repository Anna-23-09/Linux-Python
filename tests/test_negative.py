"""
Создать отдельный файл для негативных тестов. Функцию
проверки вынести в отдельную библиотеку. Повредить архив
(например, отредактировав его в текстовом редакторе).
Написать негативные тесты работы архиватора с командами
распаковки (e) и проверки (t) поврежденного архива.
"""

from checkers import negative_checkout
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)


class TestNegative:
    def test_negative_step_1(self, make_files, make_folders, make_bad_file):
        # test2
        assert negative_checkout(f"cd {data['FOLDER_OUT']}; 7z e {make_bad_file}.7z {data['FOLDER_EXTRACT']} -y",
                                 "ERROR"), "test2 Fail"

    def test_negative_step_2(self, make_files, make_folders, make_bad_file):
        # test2
        assert negative_checkout(f"cd {data['FOLDER_OUT']}; 7z t {make_bad_file}.7z {data['FOLDER_EXTRACT']} -y",
                                 "ERROR"), "test2 Fail"
