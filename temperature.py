def convertTemperature(temperature, type, convertTo):
    
    # kelvin convert to celcius
    if type == "kelvin" and convertTo == "celcius" :
        celsius = temperature - 273.15
        return f"Suhu {temperature} Kelvin dikonversi ke Celsius = {celsius} °C"
    
    # celcius convert to kelvin
    elif type == "celcius" and convertTo == "kelvin" :
        kelvin = temperature + 273.15
        return f"Suhu {temperature} Celsius dikonversi ke Kelvin = {kelvin} K"
    
    
    #  Celsius to Fahrenheit 
    elif type == "celcius" and convertTo == "fahrenheit":
        fahrenheit = (temperature * 9/5) + 32
        return f"Suhu {temperature} Celsius dikonversi ke Fahrenheit = {fahrenheit} °F"
        
    # Kelvin to fahrenheit
    elif type == "kelvin" and convertTo == "fahrenheit":
        celsius_temp = temperature - 273.15
        fahrenheit = (celsius_temp * 9/5) + 32
        return f"Suhu {temperature} Kelvin dikonversi ke Fahrenheit = {fahrenheit} °F"
    
    # Fahrenheit to Celsius
    elif type == "fahrenheit" and convertTo == "celcius":
        celsius = (temperature - 32) * 5/9
        return f"Suhu {temperature} Fahrenheit dikonversi ke Celsius = {celsius} °C"
    
    # Fahrenheit to Kelvin
    elif type == "fahrenheit" and convertTo == "kelvin":
        celsius_temp = (temperature - 32) * 5/9
        kelvin = celsius_temp + 273.15
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

