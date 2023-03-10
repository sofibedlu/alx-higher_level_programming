Update the class Base by adding the static method def draw(list_rectangles, list_squares): that opens a window and draws all the Rectangles and Squares:

You must use the Turtle graphics module (https://docs.python.org/3.0/library/turtle.html)
To install it: sudo apt-get install python3-tk
To make the GUI available outside your vagrant machine, add this line in your Vagrantfile: config.ssh.forward_x11 = true
No constraints for color, shape etc… be creative!

/*****/

guillaume@ubuntu:~/$ cat 101-main.py
#!/usr/bin/python3
""" 101-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    list_rectangles = [Rectangle(100, 40), Rectangle(90, 110, 30, 10), Rectangle(20, 25, 110, 80)]
    list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

    Base.draw(list_rectangles, list_squares)

guillaume@ubuntu:~/$ ./101-main.py
....


/***/

Uncommented line in /etc/ssh/ssh_config that said # ForwardX11 no and change no to yes.
Then added line config.ssh.forward_agent = true to my Vagrantfile in addition to config.ssh.forward_x11 = true.
Halted my vm with vagrant halt and started it back up with vagrant up --provision then vagrant ssh.
If you get an error that looks like /usr/bin/xauth: timeout in locking authority file /home/vagrant/.Xauthority, then enter rm .Xauthority (you may have to sudo).
Logout and restart the vm with vagrant up --provision.
Test with xeyes. If Xquartz is installed on the Mac OS it should open in an Xquartz window.
It is your responsibility to request a review for this task from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.
