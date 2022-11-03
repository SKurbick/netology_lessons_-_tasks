from tasks.main_example.YandexDisk_example import YandexDisk, path_token


def test_unsuccessfully_create_folder_yd(ex_status_code=409):
    yd = YandexDisk(path_token)
    status_code, folder = yd.create_folder()
    assert status_code == ex_status_code


def test_successfully_create_folder_yd(ex_status_code=201):
    yd = YandexDisk(path_token)
    status_code, folder = yd.create_folder()
    assert status_code == ex_status_code
