import random
import datetime
        
start_date = datetime.date(1909, 8, 21)
end_date = datetime.date(2026, 8, 25)
list_dates = []
chosen_dates = []
delta = datetime.timedelta(days=1)

while start_date <= end_date:
    list_dates.append(start_date)
    start_date += delta

chosen_dates.append(random.choice(list_dates))

while True:
    random_day = random.choice(list_dates)
    for i in chosen_dates:
        if i == random_day:
            chosen_dates.append(random_day)
            print(f"\n{len(chosen_dates)}\n{random_day}")
            exit()
    else:
        chosen_dates.append(random_day) 