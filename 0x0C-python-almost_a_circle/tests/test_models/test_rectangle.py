""" unittest models/rectangle.py module"""

from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangle_constructor(unittest.TestCase):
    """unittest for constructor method in Rectangle class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_with_mandatory_arg(self):
        A = Rectangle(1, 2)
        self.assertEqual(A.width, 1)
        self.assertEqual(A.height, 2)
        self.assertEqual(A.x, 0)
        self.assertEqual(A.y, 0)
        self.assertEqual(A.id, 1)

    def test_three_args(self):
        A = Rectangle(1, 2, 3)
        self.assertEqual(A.id, 1)

    def test_four_args(self):
        A = Rectangle(1, 2, 3, 4)
        self.assertEqual(A.id, 1)

    def test_full_parametrs(self):
        A = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(A.id, 5)

    def test_two_rectangle(self):
        A = Rectangle(1, 2)
        B = Rectangle(2, 2)
        self.assertEqual(A.id, 1)
        self.assertEqual(B.id, 2)

    def test_empty_arg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_empty_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_six_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_private_width_attr(self):
        A = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            A.__width

    def test_private_height_attr(self):
        A = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            A.__height

    def test_private_x_attr(self):
        A = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            A.__x

    def test_private_y_attr(self):
        A = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            A.__y


class TestRectang_width_attribute(unittest.TestCase):
    """unittest for private width attribute in Rectangle class"""

    def test_width_getter(self):
        A = Rectangle(2, 2)
        self.assertEqual(A.width, 2)

    def test_width_setter(self):
        A = Rectangle(2, 2)
        A.width = 6
        self.assertEqual(A.width, 6)

    def test_zero_width(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(0, 3)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_negative_width(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(-3, 1)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_float_width(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(2.3, 4)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_string_width(self):
        with self.assertRaises(TypeError) as err:
            Rectangle("abc", 4)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_list_width(self):
        with self.assertRaises(TypeError) as err:
            Rectangle([1], 4)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_tuple_width(self):
        with self.assertRaises(TypeError) as err:
            Rectangle((2,), 4)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_dict_width(self):
        with self.assertRaises(TypeError) as err:
            Rectangle({'a': 2}, 4)
        self.assertEqual(str(err.exception), "width must be an integer")


class TestRectangle_private_height_attribute(unittest.TestCase):
    """unittest for private height attribute in Rectangle class"""

    def test_height_getter(self):
        A = Rectangle(2, 3)
        self.assertEqual(A.height, 3)

    def test_height_setter(self):
        A = Rectangle(1, 3)
        A.height = 9
        self.assertEqual(A.height, 9)

    def test_zero_height(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(2, 0)
        self.assertEqual(str(err.exception), "height must be > 0")

    def test_negative_height(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(2, -2)
        self.assertEqual(str(err.exception), "height must be > 0")

    def test_list_height(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(2, [5])
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_dict_height(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(2, {})
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_float_height(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(2, 6.9)
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_string_height(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(2, "abc")
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_tuple_height(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(3, (3, 2))
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_None_height(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(3, None)
        self.assertEqual(str(err.exception), "height must be an integer")


class TestRectangle_private_x_attribute(unittest.TestCase):
    """unittest for private x attribute in Rectangle class"""

    def test_x_getter(self):
        A = Rectangle(1, 2, 3, 4)
        self.assertEqual(A.x, 3)

    def test_x_setter(self):
        A = Rectangle(1, 2, 3, 4)
        A.x = 9
        self.assertEqual(A.x, 9)

    def test_negative_x(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(1, 2, -5, 3)
        self.assertEqual(str(err.exception), "x must be >= 0")

    def test_float_x(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(2, 3, 7.3, 5)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_list_x(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(2, 3, [1], 5)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_dict_x(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(2, 3, {'x': 1}, 5)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_tuple_x(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(2, 3, (1,), 5)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_string_x(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(2, 3, 'a', 5)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_None_x(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(2, 3, None, 5)
        self.assertEqual(str(err.exception), "x must be an integer")


class TestRectangle_private_y_attribute(unittest.TestCase):
    """unittest for private y attribute in Rectangle class"""

    def test_y_getter(self):
        A = Rectangle(1, 2, 3, 4)
        self.assertEqual(A.y, 4)

    def test_y_setter(self):
        A = Rectangle(1, 2, 3, 4)
        A.y = 9
        self.assertEqual(A.y, 9)

    def test_negative_y(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(1, 2, 5, -3)
        self.assertEqual(str(err.exception), "y must be >= 0")

    def test_float_y(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(2, 3, 7, 5.2)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_list_y(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(2, 3, 1, [5])
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_dict_y(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(2, 3, 1, {})
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_tuple_y(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(2, 3, 1, (5,))
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_string_y(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(2, 3, 1, '5')
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_None_y(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(2, 3, 5, None)
        self.assertEqual(str(err.exception), "y must be an integer")


class TestRectangle_area(unittest.TestCase):
    """unittest for area method in Rectangle class"""

    def test_Rectangle_area(self):
        A = Rectangle(2, 3, 1, 1, 2)
        self.assertEqual(A.area(), 6)

    def test_area_after_changing_attr_value(self):
        A = Rectangle(2, 3, 1, 1, 2)
        self.assertEqual(A.area(), 6)
        A.width = 5
        A.height = 4
        self.assertEqual(A.area(), 20)

    def test_area_with_arg(self):
        A = Rectangle(2, 3, 1, 1, 2)
        with self.assertRaises(TypeError):
            A.area(2)


class TestRectangle_str(unittest.TestCase):
    """unittest for __str__ method in Rectangle class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_one_Rectangle(self):
        A = Rectangle(2, 1, 4, 3, 5)
        self.assertEqual(str(A), "[Rectangle] (5) 4/3 - 2/1")

    def test_Rectangle_with_two_arg(self):
        A = Rectangle(4, 3)
        self.assertEqual(str(A), "[Rectangle] (1) 0/0 - 4/3")

    def test_two_Rectangle(self):
        A = Rectangle(2, 7, 5)
        B = Rectangle(3, 3, 1, 2, 8)
        self.assertEqual(str(A), "[Rectangle] (1) 5/0 - 2/7")
        self.assertEqual(str(B), "[Rectangle] (8) 1/2 - 3/3")


class TestRectangle_update(unittest.TestCase):
    """unittest for update method in Rectangle class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_args_parameter(self):
        A = Rectangle(2, 1, 5, 4, 7)
        self.assertEqual(str(A), "[Rectangle] (7) 5/4 - 2/1")
        A.update(5, 6, 1, 1, 3)
        self.assertEqual(str(A), "[Rectangle] (5) 1/3 - 6/1")

    def test_args_with_one_arg(self):
        A = Rectangle(2, 1, 5, 4, 7)
        self.assertEqual(str(A), "[Rectangle] (7) 5/4 - 2/1")
        A.update(2)
        self.assertEqual(str(A), "[Rectangle] (2) 5/4 - 2/1")

    def test_args_with_two_arg(self):
        A = Rectangle(2, 1, 5, 4, 7)
        self.assertEqual(str(A), "[Rectangle] (7) 5/4 - 2/1")
        A.update(2, 3)
        self.assertEqual(str(A), "[Rectangle] (2) 5/4 - 3/1")

    def test_args_with_four_arg(self):
        A = Rectangle(2, 1, 5, 4, 7)
        self.assertEqual(str(A), "[Rectangle] (7) 5/4 - 2/1")
        A.update(2, 3, 3)
        self.assertEqual(str(A), "[Rectangle] (2) 5/4 - 3/3")

    def test_args_with_None_id(self):
        A = Rectangle(2, 1, 5, 4, 7)
        self.assertEqual(str(A), "[Rectangle] (7) 5/4 - 2/1")
        A.update(None)
        self.assertEqual(str(A), "[Rectangle] (7) 5/4 - 2/1")

    def test_args_negative_width(self):
        A = Rectangle(2, 1, 5, 4, 7)
        with self.assertRaises(ValueError) as err:
            A.update(3, -3, 6, 4, 8)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_args_string_height(self):
        A = Rectangle(2, 1, 5, 4, 7)
        with self.assertRaises(TypeError) as err:
            A.update(1, 2, "abc", 4, 5)
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_args_negative_x(self):
        A = Rectangle(2, 1, 5, 4, 7)
        with self.assertRaises(ValueError) as err:
            A.update(3, 4, 6, -4, 8)
        self.assertEqual(str(err.exception), "x must be >= 0")

    def test_args_float_y(self):
        A = Rectangle(2, 1, 5, 4, 7)
        with self.assertRaises(TypeError) as err:
            A.update(1, 2, 5, 4, 5.78)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_kwargs_with_one_kwarg(self):
        A = Rectangle(2, 1, 5, 4, 7)
        self.assertEqual(str(A), "[Rectangle] (7) 5/4 - 2/1")
        A.update(height=3)
        self.assertEqual(str(A), "[Rectangle] (7) 5/4 - 2/3")

    def test_kwargs_two_kwarg(self):
        A = Rectangle(2, 1, 5, 4, 7)
        self.assertEqual(str(A), "[Rectangle] (7) 5/4 - 2/1")
        A.update(id=10, width=9)
        self.assertEqual(str(A), "[Rectangle] (10) 5/4 - 9/1")

    def test_kwargs_with_all_attr(self):
        A = Rectangle(2, 1, 5, 4, 7)
        self.assertEqual(str(A), "[Rectangle] (7) 5/4 - 2/1")
        A.update(height=4, id=4, width=4, x=4, y=4)
        self.assertEqual(str(A), "[Rectangle] (4) 4/4 - 4/4")

    def test_kwargs_with_None_id(self):
        A = Rectangle(2, 3)
        self.assertEqual(str(A), "[Rectangle] (1) 0/0 - 2/3")
        A.update(id=None)
        self.assertEqual(str(A), "[Rectangle] (1) 0/0 - 2/3")

    def test_kwargs_with_dict_input(self):
        A = Rectangle(2, 1, 5, 4, 7)
        self.assertEqual(str(A), "[Rectangle] (7) 5/4 - 2/1")
        A.update(**{'x': 6, 'y': 7, 'id': 33, 'height': 4, 'width': 3})
        self.assertEqual(str(A), "[Rectangle] (33) 6/7 - 3/4")

    def test_kwargs_with_negative_width(self):
        A = Rectangle(2, 1, 5, 4, 7)
        with self.assertRaises(ValueError) as err:
            A.update(width=-3)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_kwargs_with_zero_width(self):
        A = Rectangle(2, 1, 5, 4, 7)
        with self.assertRaises(ValueError) as err:
            A.update(width=0)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_kwargs_with_list_height(self):
        A = Rectangle(2, 1, 5, 4, 7)
        with self.assertRaises(TypeError) as err:
            A.update(height=[2])
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_kwargs_with_negative_x(self):
        A = Rectangle(2, 1, 5, 4, 7)
        with self.assertRaises(ValueError) as err:
            A.update(x=-3)
        self.assertEqual(str(err.exception), "x must be >= 0")

    def test_kwargs_with_string_y(self):
        A = Rectangle(2, 1, 5, 4, 7)
        with self.assertRaises(TypeError) as err:
            A.update(y="abc")
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_args_and_kwargs_same_time(self):
        A = Rectangle(2, 1, 5, 4, 7)
        self.assertEqual(str(A), "[Rectangle] (7) 5/4 - 2/1")
        A.update(3, 1, 6, width=77, height=40)
        self.assertEqual(str(A), "[Rectangle] (3) 5/4 - 1/6")


class TestRectangle_to_dictionary(unittest.TestCase):
    """unittest for to_dictionary method in Rectangle class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_to_dictionary_result(self):
        A = Rectangle(3, 1)
        expected = {'id': 1, 'width': 3, 'height': 1, 'x': 0, 'y': 0}
        self.assertDictEqual(A.to_dictionary(), expected)

    def test_to_dictionary_with_two_Rectangle(self):
        A = Rectangle(2, 3, 4, 1, 5)
        B = Rectangle(1, 2, 3, 4, 5)
        A.update(**B.to_dictionary())
        self.assertDictEqual(A.to_dictionary(), B.to_dictionary())

    def test_to_dictionary_with_arg(self):
        A = Rectangle(2, 3, 4, 1, 5)
        with self.assertRaises(TypeError):
            A.to_dictionary(3)


if __name__ == "__main__":
    unittest.main()
