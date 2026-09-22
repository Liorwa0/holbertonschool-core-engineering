#!/usr/bin/env python3
"""Defines abstract Animal class and its subclasses Dog and Cat."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound of the animal."""
        pass


class Dog(Animal):
    """Represent a Dog."""

    def sound(self):
        """Return dog's sound."""
        return "Bark"


class Cat(Animal):
    """Represent a Cat."""

    def sound(self):
        """Return cat's sound."""
        return "Meow"
