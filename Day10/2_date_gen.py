import pandas as pd

start_date = '01-01-2024'
end_date = '15-01-2024'
date_range = pd.date_range(start=start_date, end=end_date)
# print(date_range)

date_series = pd.Series(date_range)

range_start = '2024-01-05'
range_end =  '2024-01-10'
sorted_dates = date_series[(date_series >= range_start) & (date_series <= range_end)]

print("original dates:")
print(date_series)
print("output dates ")
print(sorted_dates)

