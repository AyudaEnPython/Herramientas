from datetime import date


def get_days(year):
    today_ = date.today()
    dob = date(int(year), 1, 1)
    return (today_ - dob).days
