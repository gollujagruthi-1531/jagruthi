celsius = input("ENTER TEMPERATURE IN CELSIUS: ")
celsius = float(celsius)

fahrenheit = celsius * 9/5 + 32
print("Temperature in Fahrenheit:", fahrenheit)

if celsius < 0:
    print("VERY COLD! WEAR THICK JACKET")
elif celsius <= 15:
    print("COLD. WEAR JACKET")
elif celsius <= 25:
    print("NICE WEATHER")
else:
    print("HOT! STAY HYDRATED")
