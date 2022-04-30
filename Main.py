# import the module
import python_weather
import asyncio

async def getweather():
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)
    Python_Weather = input("Enter Place in Python:\n")
    # fetch a weather forecast from a city
    weather = await client.find(Python_Weather)

    # returns the current day's forecast temperature (int)
    print((weather.current.temperature - 32)*5/9)

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, (forecast.temperature-32)*5/9)

    # close the wrapper once done
    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())