#!/usr/bin/python3
"""Defines a file-appeding function."""


def append_write(filename="", text=""):
    """ Appends a string to the end of a text file (UTF-8) and returns the number of characters add.
    Args:
        filename (str): The name of the file.
        text (str): The text to be appended to the file.
    Returns:
        int: The number of characters added.

    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
