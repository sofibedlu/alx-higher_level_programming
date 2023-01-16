"""unittest documentation for base module"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import os


class TestBase__init__(unittest.TestCase):
    """unittest for constractur method of the Base class
    """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_with_no_id(self):
        A = Base()
        B = Base()
        self.assertEqual(A.id, 1)
        self.assertEqual(B.id, 2)

    def test_more_than_2(self):
        """instantiate more than two insatnces with no id"""
        A = Base()
        B = Base()
        C = Base()
        self.assertEqual(A.id, C.id - B.id)

    def test_None_id(self):
        A = Base(None)
        B = Base(None)
        self.assertEqual(A.id, B.id - 1)

    def test_int_id(self):
        A = Base(1)
        B = Base(4)
        self.assertEqual(A.id, 1)
        self.assertEqual(B.id, 4)

    def test_mix(self):
        """instantiat both with no id and with id(int)"""
        A = Base(4)
        B = Base()
        C = Base(None)
        self.assertEqual(A.id, 4)
        self.assertEqual(B.id, 1)
        self.assertEqual(C.id, 2)

    def test_set_value_id(self):
        """test if the value id would be changed after instantiation"""
        A = Base(7)
        A.id = 8
        self.assertEqual(A.id, 8)

    def test_string_id(self):
        A = Base("abc")
        self.assertEqual(A.id, "abc")

    def test_list_id(self):
        A = Base([1, 2, 3])
        self.assertEqual(A.id, [1, 2, 3])

    def test_set_id(self):
        A = Base({1, 2, 3})
        self.assertEqual(A.id, {1, 2, 3})

    def test_dict_id(self):
        A = Base({'a': 1})
        self.assertEqual(A.id, {'a': 1})

    def test_float_id(self):
        A = Base(5.06)
        self.assertEqual(A.id, 5.06)

    def test_tuple_id(self):
        A = Base((1, 2, 3))
        self.assertEqual(A.id, (1, 2, 3))

    def test_with_two_arg(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """unittest for to_json_string method in Base class"""
    def setUp(self):
        Base._base__nb_objects = 0

    def test_None_list(self):
        j_str = Base.to_json_string(None)
        self.assertEqual(j_str, "[]")

    def test_empty_list(self):
        j_str = Base.to_json_string([])
        self.assertEqual(j_str, "[]")

    def test_list_of_dictionary(self):
        j_str = Base.to_json_string([{'a': 1}, {'b': 2}])
        self.assertEqual(j_str, '[{"a": 1}, {"b": 2}]')

    def test_return_type(self):
        """test return type of to_json_method"""
        listt = Base.to_json_string([{'a': 1}])
        self.assertEqual(str, type(listt))

    def test_Rectangle_ins(self):
        """test to_json_string method on instances of a class who inherites
            the Base class like Rectangle or
            Square that inherites from Rectangle
        """
        A = Rectangle(1, 1)
        self.assertTrue(len(A.to_json_string([A.to_dictionary()])) == 52)
        self.assertTrue(type(A.to_json_string([A.to_dictionary()]) == str))

    def test_Square_ins(self):
        A = Square(1)
        self.assertTrue(len(A.to_json_string([A.to_dictionary()])) == 38)
        self.assertTrue(type(A.to_json_string([A.to_dictionary()]) == str))

    def test_Rectangle_more_than_one_ins(self):
        A = Rectangle(1, 1)
        B = Rectangle(2, 2)
        r1 = A.to_dictionary()
        r2 = B.to_dictionary()
        self.assertTrue(len(Rectangle.to_json_string([r1, r2])) == 104)

    def test_Square_more_than_one_ins(self):
        A = Square(1)
        B = Square(2)
        s1 = A.to_dictionary()
        s2 = B.to_dictionary()
        self.assertTrue(len(Square.to_json_string([s1, s2])) == 76)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_extra_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])


class TestBase_save_to_file(unittest.TestCase):
    """unittest for save_to_file method in Base class"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_None_arg(self):
        Rectangle.save_to_file(None)
        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            read = f.read()
        self.assertEqual(read, "[]")

    def test_Rectangle_inst(self):
        Rectangle.save_to_file([Rectangle(1, 2, 3, 4, 5)])
        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            self.assertTrue(len(f.read()) == 52)

    def test_more_than_one_Rec(self):
        Rectangle.save_to_file([Rectangle(1, 2, 3, 4, 5),
                                Rectangle(3, 4, 1, 7, 2)])
        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            self.assertTrue(len(f.read()) == 104)

    def test_Square_int(self):
        Square.save_to_file([Square(1, 2, 3, 4)])
        with open('Square.json', 'r') as f:
            self.assertTrue(len(f.read()) == 38)

    def test_more_Square(self):
        Square.save_to_file([Square(1, 2, 3, 4), Square(3, 2, 4, 1)])
        with open('Square.json', 'r') as f:
            self.assertTrue(len(f.read()) == 76)

    def test_empty_list(self):
        Rectangle.save_to_file([])
        with open('Rectangle.json', 'r') as f:
            self.assertTrue(f.read() == "[]")

    def test_empty_arg(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()
            Square.save_to_file()

    def test_extra_arg(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(1, [Rectangle(1, 2, 3, 4, 5)])


class TestBase_from_json_string(unittest.TestCase):
    """unittest for from_json_string method in Base class"""

    def test_None_arg(self):
        li_ob = Base.from_json_string(None)
        self.assertEqual(li_ob, [])

    def test_empty_list_arg(self):
        li_ob = Base.from_json_string('[]')
        self.assertEqual(li_ob, [])

    def test_Rectangle_inst(self):
        A = Rectangle(1, 2, 3, 4, 5)
        js_str = A.to_json_string([A.to_dictionary()])
        li_ob = Base.from_json_string(js_str)
        self.assertEqual(li_ob, [A.to_dictionary()])

    def test_two_Rectangle(self):
        A = Rectangle(1, 2, 3, 4, 5)
        B = Rectangle(3, 5, 7, 2, 7)
        js_str = A.to_json_string([A.to_dictionary(), B.to_dictionary()])
        li_ob = Base.from_json_string(js_str)
        self.assertEqual(li_ob, [A.to_dictionary(), B.to_dictionary()])

    def test_Square(self):
        A = Square(1, 2, 3, 4)
        js_str = A.to_json_string([A.to_dictionary()])
        li_ob = Base.from_json_string(js_str)
        self.assertEqual(li_ob, [A.to_dictionary()])

    def test_two_Square(self):
        A = Square(1, 2, 3, 4)
        B = Square(3, 4, 5, 1)
        js_str = A.to_json_string([A.to_dictionary(), B.to_dictionary()])
        li_ob = Base.from_json_string(js_str)
        self.assertEqual(li_ob, [A.to_dictionary(), B.to_dictionary()])

    def test_empty_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_extra_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string("[]", "[{'x': 1}]")


class TestBase_create(unittest.TestCase):
    """unittest for create method in Base class"""

    def test_Rectangle(self):
        A = Rectangle(1, 2, 3, 4, 5)
        B = Rectangle.create(**A.to_dictionary())
        self.assertEqual(A.to_dictionary(), B.to_dictionary())

    def test_type_of_new_Rectangle(self):
        A = Rectangle(1, 2, 3, 4, 5)
        B = Rectangle.create(**A.to_dictionary())
        self.assertTrue(B.__class__.__name__ == 'Rectangle')

    def test_display_Rectangle(self):
        A = Rectangle(1, 2, 3, 4, 5)
        B = Rectangle.create(**A.to_dictionary())
        self.assertEqual(str(A), "[Rectangle] (5) 3/4 - 1/2")
        self.assertEqual(str(B), "[Rectangle] (5) 3/4 - 1/2")

    def test_not_equal_Rectangle(self):
        A = Rectangle(1, 2, 3, 4, 5)
        B = Rectangle.create(**A.to_dictionary())
        self.assertNotEqual(A, B)

    def test_The_Rectangle_is_not(self):
        A = Rectangle(1, 2, 3, 4, 5)
        B = Rectangle.create(**A.to_dictionary())
        self.assertIsNot(A, B)

    def test_Square(self):
        A = Square(1, 2, 3, 4)
        B = Square.create(**A.to_dictionary())
        self.assertEqual(A.to_dictionary(), B.to_dictionary())

    def test_type_of_new_Square(self):
        A = Square(1, 2, 3, 4)
        B = Square.create(**A.to_dictionary())
        self.assertTrue(B.__class__.__name__ == 'Square')

    def test_display_Square(self):
        A = Square(1, 2, 3, 4)
        B = Square.create(**A.to_dictionary())
        self.assertEqual(str(A), "[Square] (4) 2/3 - 1")
        self.assertEqual(str(B), "[Square] (4) 2/3 - 1")

    def test_not_equal_Square(self):
        A = Square(1, 2, 3, 4)
        B = Square.create(**A.to_dictionary())
        self.assertNotEqual(A, B)

    def test_The_Square_is_not(self):
        A = Square(1, 2, 3, 4)
        B = Square.create(**A.to_dictionary())
        self.assertIsNot(A, B)


class TestBase_load_from_file(unittest.TestCase):
    """unittest for load_from_file method in Base class"""

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_Rectangle_from_file(self):
        A = Rectangle(1, 2, 3, 4, 5)
        B = Rectangle(3, 4, 7, 5, 1)
        Rectangle.save_to_file([A, B])
        list_obj = Rectangle.load_from_file()
        self.assertEqual(str(list_obj[0]), str(A))
        self.assertEqual(str(list_obj[1]), str(B))

    def test_load_Square_from_file(self):
        A = Square(1, 2, 3, 4)
        B = Square(3, 2, 1, 2)
        Square.save_to_file([A, B])
        list_obj = Square.load_from_file()
        self.assertEqual(str(list_obj[0]), str(A))
        self.assertEqual(str(list_obj[1]), str(B))

    def test_return_type_from_file(self):
        A = Square(1, 2, 3, 4)
        B = Square(3, 2, 1, 2)
        Square.save_to_file([A, B])
        list_obj = Square.load_from_file()
        self.assertTrue(type(list_obj), list)

    def test_Type_from_the_list_Rectangle(self):
        A = Rectangle(1, 2, 3, 4, 5)
        B = Rectangle(3, 4, 7, 5, 1)
        Rectangle.save_to_file([A, B])
        list_obj = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in list_obj))

    def test_Type_from_the_list_Square(self):
        A = Square(1, 2, 3, 4)
        B = Square(3, 2, 1, 2)
        Square.save_to_file([A, B])
        list_obj = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in list_obj))

    def test_load_from_not_exist_file(self):
        list_obj = Square.load_from_file()
        self.assertEqual(list_obj, [])

    def test_pass_extra_arg(self):
        with self.assertRaises(TypeError):
            Square.load_from_file([])


if __name__ == "__main__":
    unittest.main()
