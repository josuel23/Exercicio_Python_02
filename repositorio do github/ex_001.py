# Exercicio de conversão de temperatura de Celsious para Fahrenheit

c = float(input('digite a temperatura em °C:'))

f = (9 * c / 5) + 32          # A ordem de precedência da expressão é exatamente a ordem que os operadores aparecem!

print(f' A temperatura de:{c:.2f}°C corresponde a:{f:.2f}°F')
