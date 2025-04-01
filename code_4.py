import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year, country_code):
    # REDID BELOW CODE Convert 'date' column to datetime format to allow tracking only 'year'
    df['year'] = pd.to_datetime(df['date']).dt.year
    #REDID BELOW CODE query method to filter data from input, @ is used to recall each variable from function in order to not include an EXTRA query statement variable, I included the A.I reference in the comments below
    data_rows = df.query('year == @year and iso_a3 == @country_code')
    
    # REDID BELOW CODE Calculate the mean of the 'dollar_price' column for the filtered rows from query method
    mean_price = data_rows['dollar_price'].mean()
    
    # Return the rounded mean
    return (round(mean_price, 2))

def get_big_mac_price_by_country(country_code):
    #REDID BELOW CODE query() method
    data_rows = df.query('iso_a3 == @country_code')
    
    #REDID BELOW CODE Calculate the mean of the 'dollar_price' column for the filtered rows from query method
    mean_price = data_rows['dollar_price'].mean()
    
    #REDID BELOW CODE Return the year, country code, and rounded mean
    return (round(mean_price, 2))


def get_the_cheapest_big_mac_price_by_year(year):
    #REDID BELOW CODE Convert 'date' column to datetime format to allow tracking only 'year'
    df['year'] = pd.to_datetime(df['date']).dt.year
    
    #REDID BELOW CODE query() method
    data_rows = df.query('year == @year')
    
    #REDID BELOW CODE Find the cheapest price from apply method
    cheapest_price = data_rows['dollar_price'].min()
    
    # Return the year, country code, and cheapest price
    return ((round(cheapest_price, 2)))

def get_the_most_expensive_big_mac_price_by_year(year):
    #REDID BELOW CODE Convert 'date' column to datetime format to allow tracking only 'year'
    df['year'] = pd.to_datetime(df['date']).dt.year
    
    #REDID BELOW CODE query() method
    data_rows = df.query('year == @year')
    
    #REDID BELOW CODE Find the cheapest price from apply method
    expensive_price = data_rows['dollar_price'].max()
    
    # Return the year, country code, and HIGHEST price
    return ((round(expensive_price, 2)))

if __name__ == "__main__":
#Mean by year and country function, I used this line seperator to create section and clearly see the different function outputs
    print("-"*20)
    year = int(input('Enter the year: '))  # Convert input to an integer
    country_code = input('Enter the country code: ').upper()

    # Call the function
    result_a = get_big_mac_price_by_year(year, country_code)

    # Print the result
    print(f'The average Big Mac price in {country_code} for the year {year} is: {result_a}')
#Mean by only country function
    print("-"*20)
    country_code = input('Enter the country code: ').upper()

    # Call the function
    result_b = get_big_mac_price_by_country(country_code)

    # Print the result
    print(f'The average Big Mac price in {country_code} is: {result_b}')
#Cheapest price of the year
    print("-"*20)
    year = int(input('Enter the year: '))  # Convert input to an integer
    result_c = get_the_cheapest_big_mac_price_by_year(year)
    print(result_c)
#Most expensive of the year
    print("-"*20)
    year = int(input('Enter the year: '))  # Convert input to an integer
    result_d = get_the_most_expensive_big_mac_price_by_year(year)
    print(result_d)

#query statements used from A.I
#Chat-GPT(version). Date of query (2025/4/1). “I am using a .query() statement in python. How can I reduce the query statements needed when recalling variables in my .query() statement?” Generated using
#OpenAI Chat-GPT. https://chat.openai.com/ 