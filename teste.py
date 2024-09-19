# 1) Cálculo de SOMA
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(f"Valor final de SOMA: {SOMA}")

# 2) Verificar se um número pertence à sequência de Fibonacci
def is_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

# 3) Cálculo de estatísticas de faturamento diário
import json

faturamento_diario = {
    "01": 1000,
    "02": 0,
    "03": 2500,
    "04": 3000,
    "05": 0,
    "06": 1500,
    "07": 3500,
    # ... mais dias com valores ou zero
}

def calcular_estatisticas(faturamento):
    valores = [v for v in faturamento.values() if v > 0]
    
    if not valores:
        print("Não há valores de faturamento disponíveis.")
        return
    
    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)
    
    dias_acima_da_media = sum(1 for v in valores if v > media_mensal)
    
    print(f"Menor valor de faturamento: R${menor_valor:.2f}")
    print(f"Maior valor de faturamento: R${maior_valor:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

calcular_estatisticas(faturamento_diario)

# 4) Percentual de faturamento por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_faturamento = sum(faturamento_estados.values())

for estado, valor in faturamento_estados.items():
    percentual = (valor / total_faturamento) * 100
    print(f"{estado}: {percentual:.2f}%")

# 5) Função para inverter uma string
def inverter_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

texto = input("Informe a string a ser invertida: ")
print(f"String invertida: {inverter_string(texto)}")
