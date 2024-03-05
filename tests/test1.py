import subprocess
import yaml
#from checkers import checkout, getout
from checkers import checkout, getout

with open('config.yaml') as f:
    data = yaml.safe_load(f)

class TestPositive:
    def test_step_1(self, make_folders, clear_folders, make_files):
        # test1
        res1 = self.checkout("cd {}; 7z a {}/arx2.".format(data["FOLDER_IN"], data["FOLDER_OUT"]), "Everything is OK")
        res2 = self.checkout("ls {}".format(data["FOLDER_OUT"]), "arx2.7z")
        assert res1 and res2, "test1 FAIL"


    def test_step_2(self, clear_folders, make_files):
        # test2
        res = []
        res.append(self.checkout("cd {}; 7z a {}/arx2.".format(data["FOLDER_IN"], data["FOLDER_OUT"]), "Everything is OK"))
        res.append(self.checkout("cd {}; 7z e arx2.7z -o{} -y".format(data["FOLDER_OUT"], data["FOLDER_EXTRACT"]), "Everything is OK"))
        for item in make_files:
            res.append(self.checkout("ls {}".format(data["FOLDER_EXTRACT"]), item)
        assert all(res), "test2 FAIL"


    def test_step_3(self):
        # test3
        assert self.checkout("cd {}; 7z t .arx2.7z".format(data["FOLDER_OUT"]), "Everything is OK"), "test3 Fail"


    def test_step_4(self):
        # test4
        assert self.checkout("cd {}; 7z d .arx2.7z".format(data["FOLDER_IN"]), "Everything is OK"), "test4 Fail"


    def test_step_5(self, clear_folders, make_files):
        # test5
        res = []
        res.append(self.checkout("cd {}; 7z a {}/arx2".format(data["FOLDER_IN"], data["FOLDER_OUT"]), "Everything is OK"))
        for item in make_files:
            res.append(self.checkout("cd {}; 7z l {}/arx2.".format(data["FOLDER_OUT"], data["FOLDER_EXTRACT"]), item))
        assert all(res), "test5 FAIL"


    def test_step_6(self, clear_folders, make_files, make_subfolder):
        #test6
        res = []
        res.append(self.checkout("cd {}; 7z a {}/arx".format(data["FOLDER_IN"], data["FOLDER_OUT"]), "Everything is OK"))
        res.append(self.checkout("cd {}; 7z x arx.7z -o{} y".format(data["FOLDER_OUT"], data["FOLDER_EXTRACT_2"]), "Everything is OK"))

        for item in make_files:
            res.append(self.checkout("ls {}".format(data["FOLDER_EXTRACT_2"]), item))

        res.append(self.checkout("ls {}".format(data["FOLDER_EXTRACT_2"]), make_subfolder[0]))
        res.append(self.checkout("ls {}/{}".format(data["FOLDER_EXTRACT_2"], make_subfolder[0]), make_subfolder[1]))
        assert all(res), "test6 FAIL"


    def test_step_7(self):
        #test7
        assert self.checkout("cd {}; 7z d arx.7z".format(data["FOLDER_OUT"]), "Everything is OK")



    def test_step_8(self, clear_folders, make_files):
        #test8
        res = []
        for item in make_files:
            res.append(self.checkout("cd {}; 7z h {}".format(data["FOLDER_IN"], item), "Everything is OK"))
            hash = getout("cd {}; crc32 {}".format(data["FOLDER_IN"], item)).upper()
            res.append(self.checkout("cd {}; 7z h {}".format(data["FOLDER_IN"], item), hash))
        assert all(res), "test8 FAIL"
