# cse-111-2023
##OpenWeatherMapAPI
The program uses environment variables to store the API key required for the OpenWeatherMap API. It also prompts the user to enter a city name, units of measurement, and whether they want current conditions or a forecast.

##User Requests
If the user requests a forecast, the program will ask if they want an hourly or 3-day forecast. The program then constructs a URL based on the user's input and sends a request to the OpenWeatherMap API to retrieve weather data.

##JSON Format
The program then checks if the response is in JSON format and if so, sanitizes the data by removing any characters that could cause issues with parsing the JSON. It then converts the sanitized data to a Python-readable dictionary and prints out the weather information in a human-readable format.

##Constructs URL
If the user requests current conditions, the program constructs a URL and sends a request to the OpenWeatherMap API to retrieve current weather data. It then sanitizes the data, converts it to a Python-readable dictionary, and prints out the weather information in a human-readable format.
