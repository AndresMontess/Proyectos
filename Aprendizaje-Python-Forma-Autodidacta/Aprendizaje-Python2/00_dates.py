### Dates ###

from datetime import datetime

now = datetime.now()

print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.year)


timestamp = now.timestamp()

print(timestamp)