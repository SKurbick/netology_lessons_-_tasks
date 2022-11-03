# import pytest
# from tasks.main_example.main_example_1 import add_new_doc
# NEW_PERSONS = [
#     ({"type": "Visa", "number": "875387", "name": "Освальд Гектор"}, 1, 1),
#     ({"type": "Passport", "number": "88 77 0584624", "name": "ПуПу ТюТю"}, 2, 2),
#     ({"type": "Document", "number": "001", "name": "Хорошее Имя"}, 3, 3)
# ]
#
#
# @pytest.mark.parametrize("new_doc, new_doc_shelf_number, num_shelf", NEW_PERSONS)
# def test_add_new_doc(new_doc, new_doc_shelf_number, num_shelf):
#     result = add_new_doc(new_doc, new_doc_shelf_number)
#     assert result == num_shelf
