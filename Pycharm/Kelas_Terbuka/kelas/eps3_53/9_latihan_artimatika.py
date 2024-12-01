# Latihan konversi satuan temperature
#
# print("\nProgram Konversi Temperature\n")
#
# celcius = float(input("Masukan suhu dalam celcius: "))
# print("suhu adalah", celcius, "celcius")
#
# reamur = (4 / 5) * celcius
# print("suhu dalam reamur adalah", reamur, "reamur")
#
# fahrenheit = ((9 / 5) * celcius) + 32
# print("suhu dalam fahrenheit adalah", fahrenheit, "fahrenheit")
#
# kelvin = celcius + 273
# print("suhu dalam kelvin adalah", kelvin, "kelvin")
#
# print(30 * "=")


# fahrenheit ke kelvin
fahrenheit = float( input( "Masukan suhu dalam fahrenheit: " ) )
print( "suhu adalah", fahrenheit, "fahrenheit" )

kelvin = 5 / 9 * (fahrenheit - 32) + 273.15
print( "suhu adalah", kelvin, "kelvin" )

print( "\nENTER\n" )
# kelvin ke fahrenheit

kelvin = float( input( "Masukan suhu dalam kelvin: " ) )
print( "suhu adalah", kelvin, "fahrenheit" )

fahrenheit = ((kelvin - 273.15) * 9 / 5 + 32)
print( "suhu adalah", fahrenheit, "fahrenheit" )
