from datetime import datetime


def convert_str_to_date(date: str):
    """
    Converts date in string format to proper date format.
    :param date: A parameter to be converted into date type.
    :return: This function return date object.
    """
    try:
        d = datetime.strptime(date, '%Y-%m-%d')
    except ValueError as ve:
        print(f'Invalid Date format. Unable to convert to Date type: {ve}')
        return datetime.now()
    return d
