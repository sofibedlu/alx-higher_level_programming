"""unittest documentation for models/square module"""

from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import unittest


class TestSquare_constructor(unittest.TestCase):
    """unittest for constructor method in Square class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_with_size_arg(self):
        A = Square(2)
        self.assertEqual(A.size, 2)
        self.assertEqual(A.width, 2)
        self.assertEqual(A.height, 2)
        self.assertEqual(A.x, 0)
        self.assertEqual(A.y, 0)
        self.assertEqual(A.id, 1)

    def test_three_args(self):
        A = Square(1, 2, 3)
        B = Square(4, 5, 6)
        self.assertEqual(A.id, 1)
        self.assertEqual(B.id, 2)

    def test_four_args(self):
        A = Square(1, 2, 3, 4)
        self.assertEqual(A.size, 1)
        self.assertEqual(A.width, 1)
        self.assertEqual(A.height, 1)
        self.assertEqual(A.x, 2)
        self.assertEqual(A.y, 3)
        self.assertEqual(A.id, 4)

    def test_empty_arg(self):
        with self.assertRaises(TypeError):
            Square()

    def test_five_arg(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)


class TestSquare_x(unittest.TestCase):
    """unittest for testing initialization of Square x attribute"""

    def test_negative_x_arg(self):
        with self.assertRaises(ValueError) as err:
            Square(1, -2, 5, 3)
        self.assertEqual(str(err.exception), "x must be >= 0")

    def test_float_x_arg(self):
        with self.assertRaises(TypeError) as err:
            Square(2, 3.4, 7, 5)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_list_x_arg(self):
        with self.assertRaises(TypeError) as err:
            Square(2, [3], 1, 5)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_dict_x_arg(self):
        with self.assertRaises(TypeError) as err:
            Square(2, {'x': 1}, 5)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_tuple_x_arg(self):
        with self.assertRaises(TypeError) as err:
            Square(2, (3,), 1, 5)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_string_x_arg(self):
        with self.assertRaises(TypeError) as err:
            Square(2, 'a', 5)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_None_x_arg(self):
        with self.assertRaises(TypeError) as err:
            Square(2, None, 5)
        self.assertEqual(str(err.exception), "x must be an integer")


class TestSquare_y(unittest.TestCase):
    """unittest for testing initialization of Square y attribute"""

    def test_negative_y(self):
        with self.assertRaises(ValueError) as err:
            Square(1, 2, -5, 3)
        self.assertEqual(str(err.exception), "y must be >= 0")

    def test_float_y(self):
        with self.assertRaises(TypeError) as err:
            Square(2, 3, 7.4, 5)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_list_y(self):
        with self.assertRaises(TypeError) as err:
            Square(2, 3, [1], 5)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_dict_y(self):
        with self.assertRaises(TypeError) as err:
            Square(2, 3, {})
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_tuple_y(self):
        with self.assertRaises(TypeError) as err:
            Square(2, 3, (1,), 5)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_string_y(self):
        with self.assertRaises(TypeError) as err:
            Square(2, 3, '1')
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_None_y(self):
        with self.assertRaises(TypeError) as err:
            Square(2, 3, None)
        self.assertEqual(str(err.exception), "y must be an integer")


class TestBase_size_attribute(unittest.TestCase):
    """unittest for size attribute in Square class"""

    def test_size_getter(self):
        A = Square(4)
        self.assertEqual(A.size, 4)

    def test_size_setter(self):
        A = Square(4)
        A.size = 6
        self.assertEqual(A.size, 6)

    def test_zero_size(self):
        with self.assertRaises(ValueError) as err:
            Square(0)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_negative_size(self):
        with self.assertRaises(ValueError) as err:
            Square(-3)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_float_size(self):
        with self.assertRaises(TypeError) as err:
            Square(2.3)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_string_size(self):
        with self.assertRaises(TypeError) as err:
            Square("abc")
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_list_size(self):
        with self.assertRaises(TypeError) as err:
            Square([1])
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_tuple_size(self):
        with self.assertRaises(TypeError) as err:
            Square((2,))
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_dict_size(self):
        with self.assertRaises(TypeError) as err:
            Square({'a': 2})
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_None_size(self):
        with self.assertRaises(TypeError) as err:
            Square(None)
        self.assertEqual(str(err.exception), "width must be an integer")


class TestSquare_str(unittest.TestCase):
    """unittest for str method in Square class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_one_Square(self):
        A = Square(2, 1, 4, 3)
        self.assertEqual(str(A), "[Square] (3) 1/4 - 2")

    def test_Square_with_two_arg(self):
        A = Square(2, 1)
        self.assertEqual(str(A), "[Square] (1) 1/0 - 2")

    def test_Square_with_three_arg(self):
        A = Square(2, 1, 4)
        self.assertEqual(str(A), "[Square] (1) 1/4 - 2")


class TestSquare_update(unittest.TestCase):
    """unittest for update method in Square class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_args_parameter(self):
        A = Square(2, 1, 5, 4)
        self.assertEqual(str(A), "[Square] (4) 1/5 - 2")
        A.update(5, 6, 1, 1)
        self.assertEqual(str(A), "[Square] (5) 1/1 - 6")

    def test_args_with_one_arg(self):
        A = Square(2, 1, 5, 4)
        self.assertEqual(str(A), "[Square] (4) 1/5 - 2")
        A.update(7)
        self.assertEqual(str(A), "[Square] (7) 1/5 - 2")

    def test_args_with_two_arg(self):
        A = Square(2, 1, 5, 4)
        self.assertEqual(str(A), "[Square] (4) 1/5 - 2")
        A.update(7, 4)
        self.assertEqual(str(A), "[Square] (7) 1/5 - 4")

    def test_args_with_three_arg(self):
        A = Square(2, 1, 5, 4)
        self.assertEqual(str(A), "[Square] (4) 1/5 - 2")
        A.update(7, 4, 9)
        self.assertEqual(str(A), "[Square] (7) 9/5 - 4")

    def test_args_with_None_id(self):
        A = Square(2, 1, 5, 4)
        self.assertEqual(str(A), "[Square] (4) 1/5 - 2")
        A.update(None)
        self.assertEqual(str(A), "[Square] (4) 1/5 - 2")

    def test_args_negative_size(self):
        A = Square(2, 1, 5, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            A.update(4, -3)

    def test_args_zero_size(self):
        A = Square(2, 1, 5, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            A.update(4, 0)

    def test_args_string_size(self):
        A = Square(2, 1, 5, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            A.update(4, "abc")

    def test_args_list_size(self):
        A = Square(2, 1, 5, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            A.update(4, [3])

    def test_args_negative_x(self):
        A = Square(2, 1, 5, 4)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            A.update(4, 3, -1)

    def test_args_dict_y(self):
        A = Square(2, 1, 5, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            A.update(4, 3, 1, [4])

    def test_kwargs_with_one_arg(self):
        A = Square(2, 1, 5, 4)
        self.assertEqual(str(A), "[Square] (4) 1/5 - 2")
        A.update(size=8)
        self.assertEqual(str(A), "[Square] (4) 1/5 - 8")

    def test_kwargs_with_two_arg(self):
        A = Square(2, 1, 5, 4)
        self.assertEqual(str(A), "[Square] (4) 1/5 - 2")
        A.update(size=8, id=12)
        self.assertEqual(str(A), "[Square] (12) 1/5 - 8")

    def test_kwargs_with_three_arg(self):
        A = Square(2, 1, 5, 4)
        self.assertEqual(str(A), "[Square] (4) 1/5 - 2")
        A.update(size=8, id=12, y=6)
        self.assertEqual(str(A), "[Square] (12) 1/6 - 8")

    def test_kwargs_with_None_id(self):
        A = Square(2, 1, 5, 4)
        self.assertEqual(str(A), "[Square] (4) 1/5 - 2")
        A.update(id=None)
        self.assertEqual(str(A), "[Square] (4) 1/5 - 2")

    def test_kwargs_with_negative_size(self):
        A = Square(2, 1, 5, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            A.update(size=-6)

    def test_kwargs_with_string_size(self):
        A = Square(2, 1, 5, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            A.update(size="abc")

    def test_kwargs_with_negative_x(self):
        A = Square(2, 1, 5, 4)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            A.update(x=-6)

    def test_kwargs_with_list_y(self):
        A = Square(2, 1, 5, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            A.update(y=[7])

    def test_args_and_kwargs_same_time(self):
        A = Square(2, 1, 5, 4)
        self.assertEqual(str(A), "[Square] (4) 1/5 - 2")
        A.update(9, 9, 9, 10, size=8, id=12, y=6)
        self.assertEqual(str(A), "[Square] (9) 9/10 - 9")


class TestSquare_to_dictionary(unittest.TestCase):
    """unittest for testing to_dictionary method in Square class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_to_dictionary_output(self):
        A = Square(4)
        expected = {'id': 1, 'size': 4, 'x': 0, 'y': 0}
        self.assertDictEqual(A.to_dictionary(), expected)

    def test_to_dictionary_with_two_Square(self):
        A = Square(2, 4, 6, 8)
        B = Square(1, 2, 3, 5)
        A.update(**B.to_dictionary())
        self.assertEqual(A.to_dictionary(), B.to_dictionary())

    def test_to_dictionary_with_arg(self):
        A = Square(2, 4, 6, 8)
        with self.assertRaises(TypeError):
            A.to_dictionary(3)


if __name__ == "__main__":
    unittest.main()
