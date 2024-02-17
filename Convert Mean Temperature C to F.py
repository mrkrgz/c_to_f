prompt="Enter the highest and lowest temperatures of a day measured in the city(°C)"

highest=float(input(prompt))
print("Highest temperature:",highest,"°C")
lowest=float(input())
print("Lowest temperature:",lowest,"°C")

MeanTemperature=(highest+lowest)/2
print("Mean Temperature in Celsius:",round(MeanTemperature,2),"°C")

highestcelcius=float(highest)
highestfahrenheit=(highestcelcius*1.8+32)
print("Highest Temperature in Fahrenheit:",round(highestfahrenheit,2))
lowestcelcius=float(lowest)
lowestfahrenheit=(lowestcelcius*1.8+32)
print("Lowest Temperature in Fahrenheit",round(lowestfahrenheit,2))
MeanTemperatureinFahrenheit=(highestfahrenheit+lowestfahrenheit)/2

print("Mean Temperature in Fahrenheit:",round(MeanTemperatureinFahrenheit,2),"°F")
