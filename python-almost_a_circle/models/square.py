"""This module contains the square object class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that represents a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method 
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation 
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update the attributes 
        """
        arg_names = ['id', 'size', 'x', 'y']
        num_args = len(args)

        for i, value in enumerate(args):
            if i >= num_args:
                break
            setattr(self, arg_names[i], value)

        if not args or num_args < 4:
            for key, value in kwargs.items():
                setattr(self, key, value)

        self.height = self.width = self.size

    def area(self):
        """Calculate and return the area.
        """

        return self.width ** 2