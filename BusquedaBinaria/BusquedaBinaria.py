import random

def generar_mil_numeros():
    numeritos = []

    for i in range(1000):
        numero = random.randint(0,10000)
        numeritos.append(numero)
        
    numeritos.sort()

    return numeritos

mil_numeros = generar_mil_numeros()
print(mil_numeros)

def busquedaBinaria(nums,num_a_buscar):
    primero = 0
    ultimo = len(nums)
    centro = int((0+len(nums))/2)

    print(f"Centro antes de: [{centro}]")
    while primero < ultimo:
        if num_a_buscar == nums[centro]:
            print(f"Se encontro el numero en el indice [{centro}]")
            return centro
        else:
            if nums[centro] < num_a_buscar:
                primero = centro+1
                centro = int((primero+ultimo)/2)
                print(f"Centro: {centro}")
            elif nums[centro] > num_a_buscar:
                ultimo = centro
                centro = int((primero+ultimo)/2)
                print(f"Centro: {centro}")
    print("No se encontro el numero")
    return False

numero_busqueda = random.randint(1,10000)
print(f"El numero a buscar es: {numero_busqueda}")
print(busquedaBinaria(mil_numeros, numero_busqueda))