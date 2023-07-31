import requests
import config

# Fetch the API key from environment variable
# The config module contains the API key as a variable called "API_KEY"
# This way, we can keep the API key separate from the main code
API_ENDPOINT = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"


# Function to get weather data from the OpenWeatherMap API for the given city
def get_weather_data(city):

    # Prepared the request parameters (city name and API)
    params = {"q": city, "appid": config.API_KEY}

    # Make a GET request to the API endpoint with the given parameters
    response = requests.get(API_ENDPOINT, params=params)

    # check if the request was successful (status code 200)
    if response.status_code == 200:

        # Convert the JSON response to a Python dictionary and return it
        return response.json()

    # If there was an error, print a message and return None
    print(f"Error: Could not retrieve data for {city}")
    return None

#Function to print the temperature for a given date from the weather data
def print_weather_temperature(data, date):

    #Loop through the weather data entries
    for entry in data["list"]:

        #Check if the given date is present in the "dt_txt" field of the current entry
        if date in entry["dt_txt"]:

            #If the date is found, extract the temperature and print it
            temp = entry["main"]["temp"]
            print(f"Temperature on {date}: {temp:.2f} °C")
            return
        
    #If the date is not found, print a message indicating on temperature data 
    print(f"No temperature data found for {date}")


#Function to print the wind speed for a given date from the weather data
def print_wind_speed(data, date):

    #Loop through the weather data entries
    for entry in data["list"]:

        #Check if the given date is present in the "dt_txt" field of the current entry
        if date in entry["dt_txt"]:

            ##If the data is found, extract the wind speed and print it
            wind_speed = entry["wind"]["speed"]
            print(f"Wind Speed on {date}: {wind_speed} m/s")
            return
    #If the date is not found, print a message indicating no wind speed data    
    print(f"No wind speed data found for {date}")


#Function to print the pressure for a given date from the weather data
def print_pressure(data, date):

    #Loop through the weather data entries
    for entry in data["list"]:
        #Check if the given date is present in the "dt_txt" field of the current entry
        if date in entry["dt_txt"]:
            #If the data is found, extract the pressure and print it
            pressure = entry["main"]["pressure"]
            print(f"Pressure on {date}: {pressure} hPa")
            return
    #If the date is not found, print a message indicating no pressure data    
    print(f"No pressure data found for {date}")


#Main function to extract the program
def main():
    #Ask the user to input the city name 
    city = input("Enter the city name (e.g., London,us): ")

    #Get weather data for the given city using the get_weather_data function
    data = get_weather_data(city)

    #If there was an error or no data was retrieved, exit the program
    if not data:
        return

    #Loop to continuously provide options until the user chooses to exit the program
    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")


        #Ask the user to input their choice
        choice = input("Enter your choice: ")

        #Process the user's choice
        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")

            #Call the print_weather_temperature function with the weather data and date
            print_weather_temperature(data, date)
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD): ")

            #Call the print_wind_speed function with the weather data and date
            print_wind_speed(data, date)
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD): ")

            #Call the print_pressure function with the weather data and date
            print_pressure(data, date)
        elif choice == "0":

            #If the user chooses to exit, print a message and break the loop
            print("Exiting the program.")
            break
        else:
            #If the user enters an invalid choice, print an error message
            print("Invalid choice. Please try again.")

#Run the main function if this script is executed directly(not imported as a module)
if __name__ == "__main__":
    main()
