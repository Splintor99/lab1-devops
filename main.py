from lib import rectangle_area, rectangle_perimeter, rectangle_diagonal


def main():
    """Задає розміри прямокутника та виводить результати обчислень."""
    length = 5
    width = 3

    area = rectangle_area(length, width)
    perimeter = rectangle_perimeter(length, width)
    diagonal = rectangle_diagonal(length, width)

    print(f"Довжина: {length}")
    print(f"Ширина: {width}")
    print(f"Площа: {area}")
    print(f"Периметр: {perimeter}")
    print(f"Діагональ: {diagonal:.2f}")


if __name__ == "__main__":
    main()
