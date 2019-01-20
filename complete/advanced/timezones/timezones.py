from datetime import datetime, timezone, timedelta

print(datetime.now()) # naive doesn't know about timezone
print(datetime.now(timezone.utc))

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)

print(today)
print(tomorrow)
print(today.strftime('%d-%m-%Y %H:%M'))

user_date = input('Enter the date in YYYY-mm-dd format: ')
user_date = datetime.strptime(user_date, '%Y-%m-%d') # str parse time

print(user_date)
