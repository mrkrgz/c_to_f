#### Mean Temperature Calculator

prompt="Enter the highest and lowest temperatures of a day measured in the city"
highest=float(input(prompt))
print("Highest temperature:",highest,"°C")
lowest=float(input(prompt))
print("Lowest temperature:",lowest,"°C")

MeanTemperature=(highest+lowest)/2
print("Mean Temperature:",round(MeanTemperature,2),"°C")