import calendar
import itertools


def get_week_later(year, month):
    generic = calendar.Calendar()
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    next_month = generic.monthdatescalendar(year, month)
    return next_month[1]


def get_previous_week(year, month):
    generic1 = calendar.Calendar()
    if month == 1:
        year -= 1
        month = 12
    else:
        month -= 1
    previous_month = generic1.monthdatescalendar(year, month)
    return previous_month[-2]



def get_days_of_month(year, month):
    inst = calendar.Calendar()
    month_complete = inst.monthdatescalendar(year, month)
    month_clean = list(itertools.chain(*month_complete))
    week_before_clean = get_previous_week(year, month)
    week_after_clean = get_week_later(year, month)
    return week_before_clean + month_clean + week_after_clean


print(get_days_of_month(2025,11))

