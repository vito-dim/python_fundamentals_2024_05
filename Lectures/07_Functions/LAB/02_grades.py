def grade(mark: float) -> str:
    """
    :param mark: float variable, representing mark given from user
    :return: string result - Fail, Poor, Good, Very Good, Excellent, depending on the input mark
    """
    mark_result = None
    if 5.50 <= mark < 6.00:
        mark_result = 'Excellent'
    elif 4.50 <= mark < 5.50:
        mark_result = 'Very Good'
    elif 3.50 <= mark < 4.50:
        mark_result = 'Good'
    elif 3.00 <= mark < 3.50:
        mark_result = 'Poor'
    elif 2.00 <= mark < 3:
        mark_result = 'Fail'

    return mark_result


current_mark = float(input())
print(grade(current_mark))
