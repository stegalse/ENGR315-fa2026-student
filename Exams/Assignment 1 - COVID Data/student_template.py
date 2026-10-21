import sys

"""
Create a program which will provide answers to the questions posed in the assignment description.
We've provided a function which will parse the NYT covid database file (named "us-counties.csv"); 
however, its correct implementation will be up to you. DO NOT MODIFY THIS FUNCTION.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.
"""


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information

    ____________________ DO NOT MODIFY THIS FUNCTION ___________________
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data


#Q1: When was the first positive case in Harrisonburg and Rockingham County?

# First, I need to add a relative path to us-counties file 
# Go up two folders, then find us-counties data
data = parse_nyt_data('../../data/covid/us-counties.csv')

# Make list to hold dates when cases were recorded in Harrisonburg and Rockingham County
harrisonburg_dates = []
rockingham_dates = []

# Label each location in tuples to corresponding data value
for entry in data: 
    date = entry[0]
    county = entry[1]
    state = entry[2]
    fips = entry[3]
    cases = entry[4]
    deaths = entry[5]
    # Find when cases were recorded in Harrisonburg and Rockingham County
    if state == 'Virginia':
        if county == 'Harrisonburg city' and cases != '0':
            harrisonburg_dates.append(date)
            continue
        elif county == 'Rockingham' and cases != '0':
            rockingham_dates.append(date)
            continue

# Find the earliest date a positive case was found and print result
harrisonburg_first = min(harrisonburg_dates)
print("First positive case in Harrisonburg:", harrisonburg_first)
rockingham_first = min(rockingham_dates)
print("First positive case in Rockingham:", rockingham_first)


#Q2: What date had the highest number of new cases in Harrisonburg and Rockingham County? 
# Make a list holding the number of cases recorded in both areas 
harrisonburg_cases = []
rockingham_cases = []

# Label each location in tuples to corresponding data value
for entry in data: 
    date = entry[0]
    county = entry[1]
    state = entry[2]
    flips = entry[3]
    cases = entry[4]
    deaths = entry[5]
    # Find when cases were in Harrisonburg and Rockingham County
    if state == 'Virginia':
        if county == 'Harrisonburg city':
            harrisonburg_cases.append((date, cases))
            continue
        elif county == 'Rockingham':
            rockingham_cases.append((date, cases))
            continue

# Find the highest number of new cases in Harrisonburg and Rockingham County in one day
harrisonburg_max_cases = max(harrisonburg_cases)
rockingham_max_cases = max(rockingham_cases)

#Find the date corresponding to the highest number of new cases then print both values
harrisonburg_max_date = harrisonburg_max_cases[0]
rockingham_max_date = rockingham_max_cases[0]
print("Highest number of new cases in Harrisonburg was", harrisonburg_max_cases[1], "on", harrisonburg_max_date)
print("Highest number of new cases in Rockingham County was", rockingham_max_cases[1], "on", rockingham_max_date)


#Q3: What seven day period had the highest number of new cases in Harrisonburg and Rockingham County? 
# Find seven days in a row where there was the most cases recorded

# Make variables to hold the maximum seven-day case counts for both locations
harrisonburg_seven_day_max = 0
rockingham_seven_day_max = 0

# Find Harrisonburg seven day max using a seven day sliding window
for i in range(len(harrisonburg_cases) - 6):
    seven_day_sum = sum(cases for date, cases in harrisonburg_cases[i:i+7])
    if seven_day_sum > harrisonburg_seven_day_max:
        harrisonburg_seven_day_max = seven_day_sum
        harrisonburg_seven_day_start_date = harrisonburg_cases[i][0]

# Find Rockingham seven day max using a seven day sliding window
for i in range(len(rockingham_cases) - 6):
    seven_day_sum = sum(cases for date, cases in rockingham_cases[i:i+7])
    if seven_day_sum > rockingham_seven_day_max:
        rockingham_seven_day_max = seven_day_sum
        rockingham_seven_day_start_date = rockingham_cases[i][0]

# Print results
print("Worst seven-day period in Harrisonburg started on", harrisonburg_seven_day_start_date, "where", harrisonburg_seven_day_max, "cases were recorded.")
print("Worst seven-day period in Rockingham County started on", rockingham_seven_day_start_date, "where", rockingham_seven_day_max, "cases were recorded.")