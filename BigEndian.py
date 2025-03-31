# Função para converter string em representação binária
def string_to_binary(s):
    return ''.join(format(ord(c), '08b') for c in s)

# Função para converter número em binário de 64 bits
def int_to_binary(n):
    return format(n, '064b')

# Função para gerar a memória em Big Endian
def gerar_memoria(nome, idade, sexo, endereco_inicial=6):
    # Converter os dados para binário
    nome_bin = string_to_binary(nome)
    idade_bin = int_to_binary(idade)
    sexo_bin = string_to_binary(sexo)

    # Como temos uma palavra de 64 bits, precisamos juntar os dados
    # Supondo que a palavra de 64 bits irá armazenar até 8 caracteres por vez
    # Portanto, o nome será dividido em várias palavras

    memoria = []
    data = nome_bin + idade_bin + sexo_bin  # Combina todos os dados em uma sequência binária
    total_bits = len(data)
    
    # Preencher a memória com palavras de 64 bits
    for i in range(0, total_bits, 64):
        memoria.append(data[i:i+64].ljust(64, '0'))  # Preencher com 0s se não preencher os 64 bits

    # Criar a matriz de memória de acordo com a tabela fornecida
    matriz = []
    for i in range(0, len(memoria), 8):
        linha = memoria[i:i+8]
        matriz.append(linha)

    return matriz

# Função para imprimir a tabela de memória
def imprimir_memoria(matriz, endereco_inicial=6):
    for i, linha in enumerate(matriz):
        print(f"{endereco_inicial + (i * 8)};", end="")
        for item in linha:
            print(f"{item};", end="")
        print()

# Dados fornecidos
nome = "Denecley Alvim Soares"
idade = 36
sexo = "Masculino"

# Gerar a memória
matriz_memoria = gerar_memoria(nome, idade, sexo)

# Imprimir a memória no formato Big Endian
imprimir_memoria(matriz_memoria)
