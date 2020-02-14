print("Si usted no es Julie, por favor matarse. Gracias")

x = input('Habib, por favor escriba su nomnbre: ')
if x == "Habib":
    print('Hello, ' + x)
elif x == "Julie": 
    print("matate habi >:c, pero bienvenido")
#break
elif x == "julie":
   print("Matate habi >:c, pero bienvenido")
#break
else :
    print("Bienvenido, pero matate habi >:c")
#break

n1 =(str(input('Digíte el primer número entero:  ')))
n2 =(str(input('Digíte el segundo número entero:  ')))

print(str('Muy bien, los números son: ' + (n1) + (" y ") +  (n2)))
if n1 > n2:
    print("El número mayor es: " + n1)
if n1 < n2:
    print("El número mayor es: " + n2)

print("la suma de ambos números es: ")
print((int(n1)) + (int(n2)))

print("la resta de ambos números es: ")
print((int(n1)) - (int(n2)))

if(int(n1) %2 == 0):
    print((n1) + "  este numero es par!")
if(int(n1) %2 != 0):
    print((n1) + "  este numero es impar!")

if(int(n2) %2 == 0):
    print((n2) + "  este numero es par!")
if(int(n2) %2 != 0):
    print((n2) + "  este numero es impar!")

