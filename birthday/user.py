import collections
from datetime import datetime, date

User = collections.namedtuple('User', ['name', 'birthday'])
week_days = ("Monday", "Tuesday", "Wednesday",
             "Thursday", "Friday", "Saturday", "Sunday")

users: list[User] = [User(name='Billy Gates', birthday=datetime(1955, 10, 20))]


def get_birthdays_per_week(users: list[User]):
    week = collections.defaultdict(list)

    today = datetime.today().date()

    for user in users:
        birthday = user.birthday.date()
        birthday_this_year: date = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year+1)
        delta_days = (birthday_this_year - today).days
        if delta_days <= 7:
            w_day = birthday_this_year.strftime('%A')
            if w_day in ('Sunday', 'Saturday'):
                week['Monday'].append(user.name)
            else:
                week[w_day].append(user.name)

    for d in week_days:
        if week[d]:
            print(f"{d}: {', '.join(week[d])}")
