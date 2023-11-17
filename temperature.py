def convertTemperature(temperature, type, convertTo):
    
    def kelvinToCelcius(temperatureKelvin):
        return temperatureKelvin - 273.15
    
    def celciusToKelvin(temperatureCelcius):
        return temperatureCelcius + 273.15
    
    def celciusToFahrenheit(temperatureCelcius):
        return (temperatureCelcius * 9/5) + 32
    
    def fahrenheitToCelcius(temperatureCelcius):
        return (temperatureCelcius - 32) * 5/9
    
    # kelvin convert to celcius
    if type == "kelvin" and convertTo == "celcius" :
        celsius = kelvinToCelcius(temperature)
        return f"Suhu {temperature} Kelvin dikonversi ke Celsius = {celsius} °C"
    
    # celcius convert to kelvin
    elif type == "celcius" and convertTo == "kelvin" :
        kelvin = celciusToKelvin(temperature)
        return f"Suhu {temperature} Celsius dikonversi ke Kelvin = {kelvin} K"
    
    
    #  Celsius to Fahrenheit 
    elif type == "celcius" and convertTo == "fahrenheit":
        fahrenheit = celciusToFahrenheit(temperature)
        return f"Suhu {temperature} Celsius dikonversi ke Fahrenheit = {fahrenheit} °F"
        
    # Kelvin to fahrenheit
    elif type == "kelvin" and convertTo == "fahrenheit":
        celsius_temp = kelvinToCelcius(temperature)
        fahrenheit = celciusToFahrenheit(celsius_temp)
        return f"Suhu {temperature} Kelvin dikonversi ke Fahrenheit = {fahrenheit} °F"
    
    # Fahrenheit to Celsius
    elif type == "fahrenheit" and convertTo == "celcius":
        celsius = fahrenheitToCelcius(temperature)
        return f"Suhu {temperature} Fahrenheit dikonversi ke Celsius = {celsius} °C"
    
    # Fahrenheit to Kelvin
    elif type == "fahrenheit" and convertTo == "kelvin":
        celsius_temp = fahrenheitToCelcius(temperature)
        kelvin = celciusToKelvin(celsius_temp)
        return f"Suhu {temperature} Fahrenheit dikonversi ke Kelvin = {kelvin} K"
    
    # Invalid conversion
    else:
        return "Konversi tidak valid. Pastikan untuk menyertakan unit yang benar ('kelvin', 'celsius', atau 'fahrenheit')."

# ? Untuk convert suhu dari kelvin ke celcius bisa menggunakan ini
print(convertTemperature(100, "kelvin", "celcius"))

# ? Untuk convert suhu dari celcius ke Kelvin bisa menggunakan ini
print(convertTemperature(100, "celcius", "kelvin"))

# ? Untuk convert suhu dari Celcius ke Fahrenheit bisa menggunakan ini
print(convertTemperature(25, "celcius", "fahrenheit"))

# ? Untuk convert suhu dari Kelvin ke Fahrenheit bisa menggunakan ini
print(convertTemperature(300, "kelvin", "fahrenheit"))

# ? Untuk convert suhu dari Fahrenheit ke Celcius bisa menggunakan ini
print(convertTemperature(98.5, "fahrenheit", "celcius"))

# ? Untuk convert suhu dari Fahrenheit ke Kelvin bisa menggunakan ini
print(convertTemperature(98.5, "fahrenheit", "kelvin"))

