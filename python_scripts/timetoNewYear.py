from datetime import datetime, timedelta

today = datetime.now()
new_year = datetime(today.year +1, month=1, day=1)
time_left = new_year - today
print(f"До НГ осталось {time_left.days} дней, {int((s := time_left.total_seconds()) / 3600)} часов, {int((s % 3600) / 60)} минут")
