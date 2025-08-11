import datetime as dt
current_time = dt.datetime.now()
print(current_time)

current_day = dt.date.today()
print(current_day)

formatted_date = current_day.strftime(('%Y'))
print(formatted_date)