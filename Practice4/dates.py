#Exercise 1: Write a Python program to subtract five days from current date.

from datetime import datetime, timedelta
# Current date and time
current_date = datetime.now()
# Subtract 5 days
new_date = current_date - timedelta(days=5)
print("Current date:", current_date)
print("Date 5 days ago:", new_date)

#Exercise 2: Write a Python program to print yesterday, today, tomorrow.

from datetime import datetime, timedelta
today = datetime.now().date()  # Get only the date part
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#Exercise 3: Write a Python program to drop microseconds from datetime.

from datetime import datetime
now = datetime.now()
no_microseconds = now.replace(microsecond=0)
print("Original datetime:", now)
print("Datetime without microseconds:", no_microseconds)

#Exercise 4: Write a Python program to calculate two date difference in seconds.

from datetime import datetime
# Example datetime values
date1 = datetime(2026, 2, 26, 12, 0, 0)
date2 = datetime(2026, 2, 25, 6, 30, 0)
# Difference in seconds
difference = (date1 - date2).total_seconds()
print("Difference in seconds:", difference) #result: Difference in seconds: 117000.0