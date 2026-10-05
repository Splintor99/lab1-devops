from lib import rectangle_area, rectangle_perimeter


def main():
    """Задає розміри прямокутника та виводить результати обчислень."""
    length = 5
    width = 3

    area = rectangle_area(length, width)
    perimeter = rectangle_perimeter(length, width)

    print(f"Довжина: {length}")
    print(f"Ширина: {width}")
    print(f"Площа: {area}")
    print(f"Периметр: {perimeter}")


if __name__ == "__main__":
    main()
