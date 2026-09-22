#!/usr/bin/env python3
"""Defines SwimMixin, FlyMixin, and Dragon classes."""


class SwimMixin:
    """Mixin providing swimming behavior."""

    def swim(self):
        """Print swim message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin providing flying behavior."""

    def fly(self):
        """Print fly message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a Dragon using mixins."""

    def roar(self):
        """Print roar message."""
        print("The dragon roars!")
