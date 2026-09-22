#!/usr/bin/env python3
"""Defines Fish, Bird, and FlyingFish classes."""


class Fish:
    """Represent a Fish."""

    def swim(self):
        """Print fish swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Print fish habitat."""
        print("The fish lives in water")


class Bird:
    """Represent a Bird."""

    def fly(self):
        """Print bird flying message."""
        print("The bird is flying")

    def habitat(self):
        """Print bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represent a FlyingFish inheriting from Fish and Bird."""

    def fly(self):
        """Print flying fish fly message."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print flying fish swim message."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print flying fish habitat."""
        print("The flying fish lives both in water and the sky!")
