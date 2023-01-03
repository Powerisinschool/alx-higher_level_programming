#!/usr/bin/python3
'''Rectangle Class
    A rectangle class
    '''


class Rectangle:
  '''Rectangle with size'''

  def __init__(self, width=0, height=0):
    '''__init__
        The __init__ method initializes the width and\
             height methods of the Rectangle.
        Attributes:
            width (:obj:'int', optional): The width of the Rectangle
            height (:obj:'int', optional): The height of the Rectangle
        Raises:
            TypeError: If 'width' or  'height' is not an integer
            ValueError: if 'width' or  'height' < 0
        '''

    if type(width) is not int:
      raise TypeError("width must be an integer")
    if width < 0:
      raise ValueError("width must be >= 0")

    if type(height) is not int:
      raise TypeError("height must be an integer")
    if height < 0:
      raise ValueError("height must be >= 0")

    self.__width = width
    self.__height = height

  @property
  def width(self):
    return self.__width

  @width.setter
  def width(self, value):
    if type(value) is not int:
      raise TypeError("width must be an integer")
    if value < 0:
      raise ValueError("width must be >= 0")
    self.__width = value

  @property
  def height(self):
    return self.__height

  @height.setter
  def height(self, value):
    if type(value) is not int:
      raise TypeError("height must be an integer")
    if value < 0:
      raise ValueError("height must be >= 0")
    self.__height = value

  def area(self):
    return (self.__width * self.__height)

  def perimeter(self):
    if width is 0 or height is 0:
      return 0
    return 2 * (self.__width + self.__height)
  