def converter(celsius: float) -> float:
    """
    Converts Celsius degrees to Fahrenheit degrees.

    Args:
        celsius (float): Celsius degrees
    Returns:
        float: Fahrenheit degrees
    Example:
        >>> print(converter(36))
        96.8
    """
    return (celsius * 9 / 5) + 32


if __name__ == "__main__":
    import doctest

    doctest.testmod()
