def calculate_area(width: int, height: int) -> int:
    """
    Function that calculates Area of a Rectangle
    :param height: (int) figure length
    :param width: (int) figure width
    :return: (int) area of the figure
    """
    area = width * height
    return area


input_width = int(input())
input_height = int(input())
result = calculate_area(height=input_height, width=input_width)

print(result)
