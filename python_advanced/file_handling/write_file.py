#!/usr/bin/env python3
"""Module for writing a string to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8) and returns written character count."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
