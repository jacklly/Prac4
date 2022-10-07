"""Ask for temperatures to convert"""
temperature_celcius = float(input("What temperature would you like in Celcius?"))
temperature_farenheit = float(input("What temperature would you like in Farenheit?"))

"""Celcius to Farenheit"""


def celcius(temperature_celcius):
    temperature_farenheit = temperature_celcius * 1.8 + 32
    print("The temperature in Farenheit from your Celcius input is: {}".format(temperature_farenheit))


"""Farenheit to Celcius"""


def farenheit(temperature_farenheit):
    temperature_celcius = (temperature_farenheit - 32) / 1.8
    print("The temperature in Celcius from your Farenheit input is: {}".format(temperature_celcius))


"""Run functions"""
celcius(temperature_celcius)
farenheit(temperature_farenheit)
