#!/usr/bin/python3
'''Rectangle Class
    This class doesn't do anything at the moment
    '''


class Rectangle:
  '''Empty class'''

  def __init__(self, width=0, height=0):
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
