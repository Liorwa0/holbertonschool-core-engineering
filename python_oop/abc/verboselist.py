#!/usr/bin/env python3
"""Defines a VerboseList class that extends list."""


class VerboseList(list):
    """A list subclass that prints notifications on modification."""

    def append(self, item):
        """Add item and print notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Extend list and print notification."""
        item_count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(item_count))

    def remove(self, item):
        """Remove item and print notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop item and print notification."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
