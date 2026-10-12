def rectangle_area(length, width):
    """Обчислює площу прямокутника за довжиною та шириною."""
    return length * width


def rectangle_perimeter(length, width):
    """Обчислює периметр прямокутника за довжиною та шириною."""
    return 2 * (length + width)


def rectangle_diagonal(length, width):
    """Обчислює діагональ прямокутника за теоремою Піфагора."""
    return (length ** 2 + width ** 2) ** 0.5
