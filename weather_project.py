#Grab a weather dataset from Chicago from 2022 in the past 4 weeks
#gather all counties temperatures
#list top 5 coldest temperatures for that period.

import pandas as pd


# print(data)

# minvalue = data['Minimum'].min()
# print(minvalue)

# coldest_temps = data.nlargest(1, ['Maximum'])
# print(coldest_temps)

#Days in which the average is below 55 degrees

# result = data[data['Average'] < 55]
# sorted_result = result.sort_values(by=['Average'])
# final_temps = sorted_result.nsmallest(5, ['Average'])

# print(final_temps)

#Let's find out how many days were there when you had a maximum temperature above 70 or a minimum temperature below 40.

def get_days_above_temperatures(temp):

    data = pd.read_csv('climate2.csv')

    hottest = data[data['Maximum'] > float(temp)]
    # coldest = data[data['Minimum'] < 25]
    total_temps = len(hottest)

    return total_temps

def get_days_below_temperatures(temp):

    data = pd.read_csv('climate2.csv')

    hottest = data[data['Minimum'] < float(temp)]
    # coldest = data[data['Minimum'] < 25]
    total_temps = len(hottest)

    return total_temps