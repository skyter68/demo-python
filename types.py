# default encoding in python 3 is UTF-8
import sys
print("encoding: " + sys.stdout.encoding)


my_string = "C'est moi là-haut !"
print(my_string)
print(u"åäö")   # u:unicode (not needed if encoding is utf8)
print("\u03bb")

my_float = 3.1415
print(my_float)

my_bool = True
print(my_bool)

my_list = ["Un", 2, 3.14]
print(my_list[1])
print(type(my_list[2]))

my_tuple = (123,"ici")
print(my_tuple[1])

my_dictionary = {"un":1, "deux":2}
print(my_dictionary["deux"])
