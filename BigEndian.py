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

    # Concatenar todos os dados em uma única sequência binária
    data = nome_bin + idade_bin + sexo_bin
    total_bits = len(data)
    
    # Lista para armazenar as palavras de 64 bits
    memoria = []
    
    # Preencher a memória com palavras de 64 bits
    for i in range(0, total_bits, 64):
        palavra = data[i:i+64].ljust(64, '0')  # Preencher com 0s se não preencher os 64 bits
        memoria.append(palavra)

    # Criar a matriz de memória de acordo com os endereços fornecidos
    matriz = []
    for i in range(0, len(memoria), 8):
        linha = memoria[i:i+8]
        matriz.append(linha)

    return matriz

# Função para imprimir a tabela de memória no formato Big Endian
def imprimir_memoria(matriz, endereco_inicial=6):
    endereco = endereco_inicial
    for linha in matriz:
        print(f"{endereco};", end="")
        for item in linha:
            print(f"{item};", end="")
        print()
        endereco += 8  # Incrementa 8 para o próximo endereço na tabela

# Dados fornecidos
nome = "Denecley Alvim Soares"
idade = 36
sexo = "Masculino"

# Gerar a memória
matriz_memoria = gerar_memoria(nome, idade, sexo)

# Imprimir a memória no formato Big Endian
imprimir_memoria(matriz_memoria)
