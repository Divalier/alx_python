""" 
Write a class Square that inherits from Rectangle (7-rectangle.py)
"""
class Square(Rectangle):
    """
    A class representing a Square shape.

    Attributes
    ----------
    __size : int
        The size of the Square object.

    Methods
    -------
    area():
        Returns the area of the Square object.
    """

    def __init__(self, size):
        """
        Constructs and initializes a new Square object with the
        specified size value.

        Parameters
        ----------
        size : int
            The size of the Square object.

        Raises
        ------
        TypeError
            If size is not an integer.
        ValueError
            If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the Square object.

        Returns
        -------
        int
            The area of the Square object.
        """
        return self.__size ** 2