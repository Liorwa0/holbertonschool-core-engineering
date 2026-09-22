#!/usr/bin/env python3
"""Module for safe_print_division function."""


def safe_print_division(a, b):
    """Divides two integers and prints result in finally block."""
    result = None
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
