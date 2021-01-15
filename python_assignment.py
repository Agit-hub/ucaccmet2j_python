# load the JSON data
import json

with open('precipitation.json') as file:
    precipitation_data = json.load(file)

# COME BACK TO: use code to read in csv file

# total=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
monthly_total=[0*12]

# select all the measurements belonging to Seattle (from the JSON data)
for measurement in precipitation_data:
    # key: station within measurement
    if measurement['station']=='GHCND:US1WAKG0038':
        # print(measurement['value'])
        print(measurement['date'].split('-')[1])
        month = measurement['date'].split('-')[1]
        month = int(month)
        # list of just seatle values
        # seatle_measurements = [measurement['date'].split('-')[1], measurement['value']]
        # print(seatle_measurements)
        monthly_total[month-1]+=measurement['value']

print(monthly_total)

# calculate the sum of the precipitation over the whole year
annual_total=[0]

# select all the measurements belonging to Seattle (from the JSON data)
for measurement in precipitation_data:
    # key: station within measurement
    if measurement['station']=='GHCND:US1WAKG0038':
        # print(measurement['value'])
        print(measurement['date'].split('-')[1])
        month = measurement['date'].split('-')[1]
        month = int(month)
        annual_total[0] += measurement['value']

print(annual_total)

# calculate the relative precipitation per month (percentage compared to the precipitation over the whole year)
