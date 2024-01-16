#!/usr/bin/python3
# models/__init__.py (empty file)

# models/base.py
class Base:
    """Base class for managing id attribute in all future classes."""

    # private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor."""
        if id is not None:
            # if id is provided, assign it to the public instance attribute
            self.id = id
        else:
            # if id is not provided, increment __nb_objects and assign it to id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

