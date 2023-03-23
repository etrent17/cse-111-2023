"""
CSE 111 Milestone
Elijah Trent
Weather Request in Python
Please set environment variable before running in Python 3

Requires API Key from OpenWeatherMap.org

User inputs city and python returns meteorological info about requested city


"""
import os
import requests
import json
import numpy

# TODO ask user if they want current conditions 
def main():
    API_KEY = get_api_key()
    if API_KEY is not False:
        print(API_KEY)
       
    else:
        print("API Key failed, please check your environment variables. Goodbye.")
        exit()
    main_url = current_condition_base()
    
    question_report = 'Do you need the current conditions or a forecast? [forecast/current] '
    question_forecast = 'Do you need hourly (12 hours), 3-day or 10-day? [hour, 3-day, 10-day] '
    question_city = 'Please input your desired city: [please no commas/spaces] '
    question_units = 'Do you use imperial units? [y/n] '
    is_imperial = ''
    
    print()
    desired_city = input(question_city)
    desired_units = input(question_units)
    desired_report = input(question_report)
    desired_forecast = input(question_forecast)
    print()

    if desired_units.lower().strip() == 'y':
        is_imperial = True
    else:
        is_imperial = False
    
    if desired_report.lower().strip() == 'forecast':
        print('forecast')
    elif desired_report.lower().strip() == 'current':
        print('current')
    else:
        print('Input not recognized, please try again.')

    if desired_forecast.lower().strip() == 'hour':
        print('hour')
    elif desired_forecast.lower().strip() == '3-day':
        print('3 day')

    elif desired_forecast.lower().strip() == '10-day':
        print('10 day')


    request_url = current_condition_url(main_url, API_KEY, desired_city)

    result = send_request(request_url)
    # print(result)
    result_as_dict = read_json_data(result)
    # print(result_as_json)
    json_check = check_for_json(result)
    # print(type(result))
    # yes_val = check_for_json(result)
    # print(yes_val)

    # make sure the data is not in JSON format so Python can understand and print accordingly
    if json_check == False:
        # print("Sanitizing JSON data")
        print()
        sanitized_data = sanitize_json_data(result_as_dict) 
        # for i in sanitized_data.items():
        #     print(i)            
        weather_info = parse_json_data(sanitized_data)
        if weather_info != None:
            print(f"The weather for {desired_city.capitalize()} right now:")
            print_weather_info(weather_info, is_imperial)
        else:
            print("The service could not find your city, please try again.")
            
    else:
        print("Failed to convert JSON to a dictionary. Please check your input and try again")

        


def get_api_key():
    try:
        #get api key from environment variables
        KEY = os.getenv('WEATHERKEY')
        if KEY is not None:
            return KEY
        else:
            return False
    except Exception as e:
        print(f"Your error: {e}")
def current_condition_base():
    #return base url for weather API
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    return base_url

def current_condition_url(base_url, api_key, name_of_city):
    #uses base url, adds api key and name of reuqested city to build proper URL
    return f"{base_url}appid={api_key}&q={name_of_city}"

def send_request(requested_url):
    #returns requested data with given url
    return requests.get(requested_url)

def read_json_data(input_data):
    #uses input data and returns it as json format
    return input_data.json()

def check_for_json(json_data):
    try:
        # print(str(json_data))
        something_json = json.loads(json_data)
    except (ValueError, TypeError) as e:
        # print(f'Your error: {e}')
        return False
    return True

def sanitize_json_data(data_in_json):
    sanitize_data = str(data_in_json).replace("'", '"').replace("True", '"True"').replace("False", '"False').replace("null", '"null"')
    result = json.loads(sanitize_data)
    return result

def from_kelvin_farenheit(kelvin):
    return kelvin * 1.8 - 459.67

def from_kelvin_celcius(kelvin):
    return kelvin - 237.15

def from_hpa_psi(hpa):
    return hpa * 0.0145037738 

def from_ms_mph(m_s):
    return m_s * 2.2369362920544025

def from_ms_kph(m_s):
    return m_s * 3.6

def parse_json_data(from_json):
    try:
        temperature_as_k = from_json['main']['temp']
        pressure_in_hpa = from_json['main']['pressure']
        humidity_in_percent = from_json['main']['humidity']
        weather_description = from_json['weather'][0]['description']
        wind = from_json['wind']['speed']
        result_list = [temperature_as_k, pressure_in_hpa, humidity_in_percent, weather_description, wind]
        
    except (ValueError, KeyError) as e:
        return None
    return result_list

def print_weather_info(weather, imperial=True):
    if imperial == True:
        temp = from_kelvin_farenheit(weather[0])
        pressure = from_hpa_psi(weather[1])
        wind = from_ms_mph(weather[4])
        print(f"Temperature: {temp:.2f} F")
        print(f"Humidity: {weather[2]}%")
        print(f"Pressure: {pressure:.2f} PSI")
        print(f"Weather Description: {weather[3]}")
        print(f"Wind: {wind:.2f} MPH")
    else:
        temp = from_kelvin_celcius(weather[0])
        wind = from_ms_kph(weather[4])
        print(f"Temperature: {temp} C")
        print(f"Pressure: {weather[1]} HPA")
        print(f"Humidity: {weather[2]}%")
        print(f"Weather Description: {weather[3]}")
        print(f"Wind: {wind:.2f} KM/H")

if __name__ == "__main__":
    main()