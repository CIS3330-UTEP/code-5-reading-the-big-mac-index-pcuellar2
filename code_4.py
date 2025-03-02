import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year: int,country_code: str):
    # Convert 'date' column to datetime format to allow tracking only 'year'
    df['date'] = pd.to_datetime(df['date'])
    
    #apply() method
    filter = df.apply(lambda row: row['date'].year == year and row['iso_a3'].lower() == country_code, axis=1)
    
    # Calculate the mean of the 'dollar_price' column for the filtered rows from apply method
    mean_price = df.loc[filter, 'dollar_price'].mean()
    
    # Return the year, country code, and rounded mean
    return (round(mean_price, 2))

def get_big_mac_price_by_country(country_code):
    pass # Remove this line and code your function

def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    year = int(input("Enter the year: "))  # Convert input to an integer
    country_code = input("Enter the country code (lowercase, 3-letter): ").strip().lower()  # Strip spaces and ensure lowercase

    # Call the function
    result_a = get_big_mac_price_by_year(year, country_code)

    # Print the result
    print(f"The average Big Mac price in {country_code} for the year {year} is: {result_a}")