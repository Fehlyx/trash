
# Diese Funktion rechnet Fahrenheit zu Celsius um.
def f_to_c(f_temp):
    c_temp = (f_temp -32) * 5/9
    #print gibt die von Fahrenheit zu Celsius umgerechnete Temperatur in Celsius an.
    print(c_temp)

# Diese Variable speichert 100° Fahrenheit als Parameter in der Funktion f_to_c.
f100_in_celsius = f_to_c(100)

# Diese Funktion rechnet Celsius zu Fahrenheit um.
def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    #print gibt die von Celsius zu Fahrenheit umgerechnete Temperatur in Fahrenheit an.
    print(f_temp)

# Diese Variable speichert 0° Celsius als Parameter in der Funktion c_to_f.
c0_in_fahrenheit = c_to_f(0)
