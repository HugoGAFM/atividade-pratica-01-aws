def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return round(gorjeta, 2)

valor = calcular_gorjeta(100.0, 15)
print(f"Gorjeta: R$ {valor:.2f}")