import calendar, locale, importlib
from datetime import timedelta

cal = calendar.Calendar(firstweekday=0)  # Monday start
# iterate month as weeks of day numbers (0 = day outside month)
for week in cal.monthdayscalendar(2025, 11):
    print(week)
# Example output for Nov 2025: [0, 0, 0, 0, 0, 1, 2] etc.

def month_dates(year, month, firstweekday=0):
    cal = calendar.Calendar(firstweekday)
    return [d for d in cal.itermonthdates(year, month) if d.month == month]

print(month_dates(2025, 11)[:3])  # first three dates

tc = calendar.TextCalendar(firstweekday=6)  # Sunday start
print(tc.formatmonth(2025, 11))  # multi-line string
# single-week header control:
print(tc.formatmonthname(2025, 11, 0, 0))


hc = calendar.HTMLCalendar(firstweekday=0)
html = hc.formatmonth(2025, 11)
print(html)
# Customize cells by overriding methods in subclass:
class MyCalendar(calendar.HTMLCalendar):
    def formatday(self, day, weekday):
        if day == 0:
            return '<td class="noday">&nbsp;</td>'
        return f'<td class="{ "weekend" if weekday>=5 else "weekday" }">{day}</td>'
    


# Localization: calendar uses locale module for names. To change language:
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')  # system must support locale
importlib.reload(calendar)  # re-reads locale-dependent names




# Next N occurrences of a weekday
def next_n_weekdays(start, weekday: int, n: int):
    # weekday: 0=Mon..6=Sun
    results = []
    d = start
    # advance to the first matching weekday
    days_ahead = (weekday - d.weekday() + 7) % 7
    if days_ahead == 0:
        days_ahead = 7  # start after today; change if include today
    d += timedelta(days=days_ahead)
    for _ in range(n):
        results.append(d)
        d += timedelta(days=7)
    return results


# Business days in month
def business_days_in_month(year, month):
    cal = calendar.Calendar()
    return [d for d in cal.itermonthdates(year, month)
            if d.month == month and d.weekday() < 5]


# Nth weekday of a month (e.g., 3rd Thursday)
def nth_weekday(year, month, weekday, n):
    cal = calendar.Calendar()
    count = 0
    for d in cal.itermonthdates(year, month):
        if d.month != month:
            continue
        if d.weekday() == weekday:
            count += 1
            if count == n:
                return d
    return None