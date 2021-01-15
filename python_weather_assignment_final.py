# load the JSON data
import json

with open('precipitation.json') as file:
    precipitation_data = json.load(file)

# Look in the CSV file, and find the station code for Seattle.

# COME BACK TO: use code to read in csv file

# total=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
monthly_total=[0]*12
print(monthly_total)
# select all the measurements belonging to Seattle (from the JSON data)
for measurement in precipitation_data:
    # key: station within measurement
    if measurement['station']=='GHCND:US1WAKG0038':
        # print(measurement['value'])
        # print(measurement['date'].split('-')[1])
        month = int(measurement['date'].split('-')[1])
        monthly_total[month-1]+=measurement['value']

# Sum all the measurement for that location for each month (i.e. create a list with the total monthly precipitation)
print(monthly_total)

# Save the results to a JSON file
with open('monthly_totals.json', 'w') as file:
    json.dump(monthly_total, file)

# calculate the sum of the precipitation over the whole year
annual_total = sum(monthly_total)
print(annual_total)

# calculate the relative precipitation per month (percentage compared to the precipitation over the whole year)

# monthly_percentage=[[monthly_total]/annual_total]

monthly_proportion=[]
for total_per_month in monthly_total:
    monthly_proportion.append(total_per_month/annual_total)

print(monthly_proportion)
