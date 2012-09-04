estatura = input("Digite su estatura en Metros: ")
peso = input("Digite su peso en Kg: ")
masa = peso / (estatura ** 2)
if masa < 18.5:
	resultado = "Estas por debajo del peso normal a tu estatura"
elif masa >= 18.5 and masa <= 24.9:
	resultado = "Tu peso se encuentra dentro de los valores normales"
elif masa <= 25.0 and masa <= 29.9:
	resultado = "Tu peso esta por encima al promedio de tu estatura"
else:
	resultado = "Presentas sintomas de Obesidad"

print "Tu masa corporal es: "
print masa
print resultado

raw_input()