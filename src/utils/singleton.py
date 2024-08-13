from functools import wraps
from typing import TypeVar, Type

T = TypeVar('T')

class _SingletonWrapper:
    """
    A singleton wrapper class. Its instances would be created
    for each decorated class.
    """

    def __init__(self, cls: Type[T]):
        wraps(cls)(self)
        self.__wrapped__ = cls
        self._instance: T = None

    def __call__(self, *args, **kwargs) -> T:
        """Returns a single instance of decorated class"""
        if self._instance is None:
            self._instance = self.__wrapped__(*args, **kwargs)
        return self._instance

    def __instancecheck__(self, instance):
        """
        Check if an instance is an instance of the wrapped class.

        Args:
            instance: The instance to check.

        Returns:
            bool: True if the instance is an instance of the wrapped class, False otherwise.
        """
        return isinstance(instance, self.__wrapped__)

    def __getattr__(self, name):
        """
        Delegate attribute access to the wrapped class.

        Args:
            name (str): The name of the attribute.

        Returns:
            Any: The value of the attribute from the wrapped class.
        """
        return getattr(self._instance, name)

def singleton(cls: Type[T]) -> Type[T]:
    """
    A singleton decorator. Returns a wrapper objects. A call on that object
    returns a single instance object of decorated class. Use the __wrapped__
    attribute to access decorated class directly in unit tests

    Args:
        cls (Type[T]): The class to be decorated.

    Returns:
        Type[T]: The singleton wrapper class.
    """
    return _SingletonWrapper(cls)

