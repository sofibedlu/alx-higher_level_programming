Write a function that adds a new attribute to an object if it’s possible:

Raise a TypeError exception, with the message "can't add new attribute" if the object can’t have new attribute
You are not allowed to use try/except
You are not allowed to import any module

/*****/

guillaume@ubuntu:~/0x0A$ cat 101-main.py
#!/usr/bin/python3
add_attribute = __import__('101-add_attribute').add_attribute

class MyClass():
    pass

mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x0A$ ./101-main.py
John
[TypeError] can't add new attribute
guillaume@ubuntu:~/0x0A$ 
