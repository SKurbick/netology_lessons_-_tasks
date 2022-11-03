import unittest
from parameterized import parameterized
from unittest.mock import patch

from tasks.main_example.main_example_1 import get_doc_owner_name, add_new_doc, delete_doc

FIXTURES_DOC_PASSPORT = [
    ("10006", 'Аристарх Павлов'),
    ("11-2", "Геннадий Покемонов"),
    ("2207 876234", "Василий Гупкин"),
]
'''
p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;

a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
 имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию,
 когда пользователь будет пытаться добавить документ на несуществующую полку.
 
d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. 
 Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
'''
FIXTURES_DOC_NUMB = [
    ("10006", True),
    ("11-2", True),
    ("2207 876234", True)
]
NEW_PERSONS = [
    ({"type": "Visa", "number": "875387", "name": "Освальд Гектор"}, '1', '1'),
    ({"type": "Passport", "number": "88 77 0584624", "name": "ПуПу ТюТю"}, '2', '2'),
    ({"type": "Document", "number": "001", "name": "Хорошее Имя"}, '3', '3')
]


#
class TestGetDocOwnerName(unittest.TestCase):
    @parameterized.expand(FIXTURES_DOC_PASSPORT)
    @patch('builtins.input')
    def test_get_doc_owner_name(self, mock_input, result, inp):
        inp.return_value = mock_input
        func_result = get_doc_owner_name()
        self.assertEqual(result, func_result)


class TestDeleteDoc(unittest.TestCase):

    @parameterized.expand(FIXTURES_DOC_NUMB)
    @patch('builtins.input')
    def test_delete_doc(self, moc_input, result, inp):
        inp.return_value = moc_input
        func_result, true_false = delete_doc()
        self.assertEqual(true_false, result)


class TestAddDoc(unittest.TestCase):
    @parameterized.expand(NEW_PERSONS)
    def test_add_new_doc(self, new_doc, new_doc_shelf_number, num_shelf):
        result = add_new_doc(new_doc, new_doc_shelf_number)
        self.assertEqual(num_shelf, result)
