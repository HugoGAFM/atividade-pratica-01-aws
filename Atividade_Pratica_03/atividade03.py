
temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F ou K): ").upper()
destino = input("Converter para (C, F ou K): ").upper()



    
if origem == "C":
        if destino == "F":
            resultado = temp * 9/5 + 32
        elif destino == "K":
            resultado = temp + 273.15
        else:
            resultado = temp

    
elif origem == "F":
        if destino == "C":
            resultado = (temp - 32) * 5/9
        elif destino == "K":
            resultado = (temp - 32) * 5/9 + 273.15
        else:
            resultado = temp

    
elif origem == "K":
        if destino == "C":
            resultado = temp - 273.15
        elif destino == "F":
            resultado = (temp - 273.15) * 9/5 + 32
        else:
            resultado = temp
else:
        print("Unidade de origem inválida.")


print(f"Temperatura convertida: {resultado:.2f} {destino}")
