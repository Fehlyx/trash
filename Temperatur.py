
# Diese Funktion rechnet Fahrenheit zu Celsius um.
print("Bitte gib die zum umrechnen gewünschte Temperatur in Fahrenheit als float oder integer an.")
f_temp = int(input())
def f_to_c(f_temp):
    c_temp = (f_temp -32) * 5/9
    return int(c_temp)
    #print gibt die von Fahrenheit zu Celsius umgerechnete Temperatur in Celsius an.
print("...° Fahrenheit ist ", f_to_c(f_temp), "° Celsius.")

print("Bitte gib die zum umrechnen gewünschte Temperatur in Celsius als float oder integer an.")
c_temp = int(input())
# Diese Funktion rechnet Celsius zu Fahrenheit um.
def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return int(f_temp)
    #print gibt die von Celsius zu Fahrenheit umgerechnete Temperatur in Fahrenheit an.
print("...° Celsius ist", c_to_f(c_temp), "° Fahrenheit.")
