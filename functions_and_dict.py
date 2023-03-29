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
    list2lweeks = next_month[0] + next_month[1]
    return list2lweeks


def get_previous_week(year, month):
    generic1 = calendar.Calendar()
    if month == 1:
        year -= 1
        month = 12
    else:
        month -= 1
    previous_month = generic1.monthdatescalendar(year, month)
    list2pweeks = previous_month[-2] + previous_month[-1]
    return list2pweeks


def get_days_of_month(year, month):
    inst = calendar.Calendar()
    month_complete = inst.monthdatescalendar(year, month)
    month_clean = set(itertools.chain(*month_complete))
    week_before_clean = get_previous_week(year, month)
    week_after_clean = get_week_later(year, month)
    return set(week_before_clean) | month_clean | set(week_after_clean)


dias = [
    'primeiro dia de trabalho',
    'segundo dia de trabalho',
    'terceiro dia de trabalho',
    'quarto dia de trabalho',
    'quinto dia de trabalho',
    'sexto dia de trabalho',
    'primeiro dia de folga',
    'segundo dia de folga',
    'terceiro dia de folga']

dias = dias *3
conversor = {}
for i in range(27):
    conversor[i-9] = dias[i]


