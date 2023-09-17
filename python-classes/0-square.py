class Square:
    """
    This class represents a square.

    Attributes:
    __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
        size (int): The size of the square.

        Note:
        The size is a private attribute.
        """
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size * self.__size

    def get_size(self):
        """
        Get the size of the square.

        Returns:
        int: The size of the square.
        """
        return self.__size

    def set_size(self, size):
        """
        Set the size of the square.

        Args:
        size (int): The new size of the square.
        """
        self.__size = size

#