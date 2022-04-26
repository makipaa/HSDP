from datetime import date


def calculate_age(birth_date):
    birth_date = date.fromisoformat(birth_date)
    current_time = date.today()
    return current_time.year - birth_date.year - ((current_time.month, current_time.day) < (birth_date.month, birth_date.day))
