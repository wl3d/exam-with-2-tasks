#Task №1
class Temperature:
    def __init__(self, temperature: float, unit: str):
        if unit not in ['K', 'C', 'F']:
            raise ValueError(f"Invalid unit '{unit}', must be one of 'K', 'C', or 'F'.")
        if (unit == 'C' and temperature < -273.15) or (unit == 'K' and temperature < 0) or (
                unit == 'F' and temperature < -459.67):
            raise ValueError(f"Temperature value is too low for the given unit: {temperature} {unit}.")

        self.temperature = temperature
        self.unit = unit

    def kelvin(self):
        if self.unit == 'K':
            raise ValueError("Temperature is already in Kelvin.")
        if self.unit == 'C':
            return self.temperature + 273.15
        if self.unit == 'F':
            return (self.temperature - 32) * 5 / 9 + 273.15

    def celsius(self):
        if self.unit == 'C':
            raise ValueError("Temperature is already in Celsius.")
        if self.unit == 'K':
            return self.temperature - 273.15
        if self.unit == 'F':
            return (self.temperature - 32) * 5 / 9

    def fahrenheit(self):
        if self.unit == 'F':
            raise ValueError("Temperature is already in Fahrenheit.")
        if self.unit == 'K':
            return (self.temperature - 273.15) * 9 / 5 + 32
        if self.unit == 'C':
            return (self.temperature * 9 / 5) + 32

    def __str__(self):
        return f"{self.temperature} {self.unit}"

try:
    temp1 = Temperature(25, 'C')
    print(temp1)
    print(f"Temperature in Kelvin: {temp1.kelvin()} K")
    print(f"Temperature in Fahrenheit: {temp1.fahrenheit()} F")

    temp2 = Temperature(300, 'K')
    print(temp2)
    print(f"Temperature in Celsius: {temp2.celsius()} C")
    print(f"Temperature in Fahrenheit: {temp2.fahrenheit()} F")

    temp3 = Temperature(100, 'F')
    print(temp3)
    print(f"Temperature in Celsius: {temp3.celsius()} C")
    print(f"Temperature in Kelvin: {temp3.kelvin()} K")

except ValueError as e:
    print(e)


#Task №2
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.quotegarden.com/mind.html')
soup = BeautifulSoup(response.content, 'html.parser')
quotes = soup.find_all('font')

for quote in quotes:
    print(quotes)
