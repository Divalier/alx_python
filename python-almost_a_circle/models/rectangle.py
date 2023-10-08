"""Write the class Square that inherits from Rectangle"""

from models.base import Base


class Rectangle(Base):
    """A class that represents a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method for Rectangle class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Square that inherits from Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """ Square that inherits from Rectangle."""


        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Square that inherits from Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """" Square that inherits from Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """int: The horizontal position of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """ Square that inherits from Rectangle."""



        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """int: The vertical position of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the vertical position of the rectangle.
        """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
    
    def area(self):
        """Calculate and return the area of the rectangle.
        """

        return self.width * self.height

    def display(self):
        """Prints the rectangle using '#' symbol.
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Return a string representation of the Rectangle instance.
        """

        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Update the attributes of the object.
        """
        arg_names = ['id', 'width', 'height', 'x', 'y']
        num_args = len(args)

        for i, value in enumerate(args):
            if i >= num_args:
                break
            setattr(self, arg_names[i], value)

        if not args or num_args < 5:
            for key, value in kwargs.items():
                setattr(self, key, value)