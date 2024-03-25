import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_all_returns_dict(self):
        self.assertIsInstance(self.storage.all(), dict)

    @patch('sys.stdout', new_callable=StringIO)
    def test_reload_no_file(self, mock_stdout):
        with patch('builtins.open', side_effect=FileNotFoundError):
            self.storage.reload()
            self.assertEqual(mock_stdout.getvalue(), "")


if __name__ == '__main__':
    unittest.main()