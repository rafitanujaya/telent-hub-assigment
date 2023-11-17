# Temperature Converter

## Deskripsi
Program ini adalah pengonversi suhu sederhana yang dapat mengubah suhu antara Kelvin, Celsius, dan Fahrenheit.

## Cara Menggunakan

### Fungsi `convertTemperature`

Fungsi ini dapat digunakan untuk mengonversi suhu antara tiga satuan: Kelvin, Celsius, dan Fahrenheit.

#### Parameter:
- `temperature` (float): Suhu yang akan dikonversi.
- `type` (str): Satuan suhu awal ('kelvin', 'celsius', atau 'fahrenheit').
- `convertTo` (str): Satuan suhu yang diinginkan ('kelvin', 'celsius', atau 'fahrenheit').

#### Contoh Penggunaan:

```python
# Untuk mengonversi suhu dari kelvin ke celcius
print(convertTemperature(100, "kelvin", "celcius"))

# Untuk mengonversi suhu dari celcius ke kelvin
print(convertTemperature(100, "celsius", "kelvin"))

# Untuk mengonversi suhu dari celcius ke fahrenheit
print(convertTemperature(25, "celsius", "fahrenheit"))

# Untuk mengonversi suhu dari kelvin ke fahrenheit
print(convertTemperature(300, "kelvin", "fahrenheit"))

# Untuk mengonversi suhu dari fahrenheit ke celcius
print(convertTemperature(98.5, "fahrenheit", "celcius"))

# Untuk mengonversi suhu dari fahrenheit ke kelvin
print(convertTemperature(98.5, "fahrenheit", "kelvin"))
