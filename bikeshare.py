import time
import pandas as pd
import numpy as np
import sys

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# change name of function to get_filter1
def get_filter1():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter the city you want to analyze bikeshare data on. Choose Washington, Chicago or NewYork: ')
    cities = ['Washington','Chicago','NewYork']
    city_found = 'N'
    for city1 in cities:
        if city1 == city.title():
            print('We will get you statistics for : {}'.format(city1))
            city_found = 'Y'
                          
    if city_found == 'N':
       print('You entered an invalid city. Enter either Chicago, Washington or New York')
#      check1 = input('\nWould you like to restart? Enter yes or no.\n')
#      if check1.lower() != 'yes':
       sys.exit(0)
       
                 
                
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Enter the month you want to analyze bikeshare data on. Choose any of the first 6 months or ALL: ')
    months = ['All','January','February','March','April','May','June']
    month_found = 'N'
    
    for month1 in months:
        if month1 == month.title():
            print('We will get you statistics for : {}'.format(month1))
            month_found = 'Y'
     
    if month_found == 'N':
       print('You entered an invalid month. Enter All or any of the first 6 months of the year')
 #      check1 = input('\nWould you like to restart? Enter yes or no.\n')
 #      if check1.lower() != 'yes':
       sys.exit(0)
       
       


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter the day you want to analyze bikeshare data on. Choose any of the 7 days in the week or ALL: ')
    day_found = 'N'
    days = ['All','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    for day1 in days:
        if day1 == day.title():
            print('We will get you statistics for : {}'.format(day1))
            day_found = 'Y'
            
    if day_found == 'N':
       print('You entered an invalid month. Enter All or any of the first 6 months of the year')
 #      check1 = input('\nWould you like to restart? Enter yes or no.\n')
 #      if check1.lower() != 'yes':
       sys.exit(0)    


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
   """
   Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
# load data file into a dataframe
   df = pd.read_csv(CITY_DATA[city])
    
# convert the Start Time column to datetime
   df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract month and day of week from Start Time to create new columns
   df['month'] = df['Start Time'].dt.month
   df['day_of_week'] = df['Start Time'].dt.weekday_name

# filter by month if applicable
   if month != 'all':
# use the index of the months list to get the corresponding int
      months = ['january', 'february', 'march', 'april', 'may', 'june']
      month = months.index(month) + 1

# filter by month to create the new dataframe
   df = df[df['month'] == month]

# filter by day of week if applicable
   if day != 'all':
# filter by day of week to create the new dataframe
      df = df[df['day_of_week'] == day.title()]
   return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

# TO DO: display the most common month
    commonth = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    for month in months:
        monthname = months[commonth - 1]
    print('common month      :',commonth) 
    print('common month name :',monthname)

#    # TO DO: display the most common day of week
    comdayofweek = df['day_of_week'].mode()[0]
    print('common day of week:',comdayofweek)
#    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.time
    comhour = df['hour'].mode()[0]
    print('common hour       :',comhour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

# TO DO: display most commonly used start station

    comstartstation = df['Start Station'].mode()[0]
    print('The most frequent start station is : ', comstartstation)
    
# TO DO: display most commonly used end station

    comendstation = df['End Station'].mode()[0]
    print('The most frequent end station is : ', comendstation)
 


# TO DO: display most frequent combination of start station and end station trip

#   print(df.groupby(['Start Station','End Station']).mode())
#    print('The most frequent start end trip: ',comtrip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

# TO DO: display total travel time
    tottravel = df['Trip Duration'].sum()    
    print('Total Travel Time   : ', tottravel)
    
# TO DO: display mean travel time
    meantravel = df['Trip Duration'].mean()    
    print('average Travel Time : ', meantravel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
#    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

# TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print('user type count : ', user_count)

# TO DO: Display counts of gender
    gender_count = df['Gender'].value_counts()
    print('gender count : ', gender_count)
    

# TO DO: Display earliest, most recent, and most common year of birth
    earliest_year = df['Birth Year'].min()
    latest_year = df['Birth Year'].max()
    common_year = df['Birth Year'].mode()[0]
    print('earliest year : ', earliest_year)
    print('latest year   : ', latest_year)
    print('common year   : ', common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
       city, month, day = get_filter1()
       df = load_data(city, month, day)
       time_stats(df)
       station_stats(df)
       trip_duration_stats(df)
       user_stats(df)

       restart = input('\nWould you like to restart? Enter yes or no.\n')
       if restart.lower() != 'yes':
          break


if __name__ == "__main__":
	main()
