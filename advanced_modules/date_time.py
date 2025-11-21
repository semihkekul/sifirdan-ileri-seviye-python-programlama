import datetime

print(dir(datetime))
# ['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']

from datetime import datetime 

print(datetime.now()) # 2025-11-21 13:59:29.229842

print(datetime.ctime(datetime.now())) # Fri Nov 21 14:47:47 2025

print(datetime.strftime(datetime.now(), "%Y ----- %X")) # 2025 ----- 14:48:48


birthday = datetime(1984, 6, 18)
print(birthday) # 1984-06-18 00:00:00
print(datetime.timestamp(birthday)) # 456357600.0 seconds
print(datetime.fromtimestamp(datetime.timestamp(birthday))) # 1984-06-18 00:00:00

print(datetime.fromtimestamp(0)) # 1970-01-01 01:00:00

print((datetime.now() - birthday).microseconds) # 59061