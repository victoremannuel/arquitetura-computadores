# Função para converter string em representação binária

def string_to_binary(s):
    return ''.join(format(ord(c), '08b') for c in s)

# Função para converter número em binário de 64 bits
def int_to_binary(n):
    return format(n, '064b')

# Função para converter binário para string
def binary_to_string(b):
    return ''.join(chr(int(b[i:i+8], 2)) for i in range(0, len(b), 8))

# Função para converter binário para número inteiro
def binary_to_int(b):
    return int(b, 2)

# Função para gerar a memória em Big Endian
def gerar_memoria(nome, idade, sexo, endereco_inicial=6):
    nome_bin = string_to_binary(nome)
    idade_bin = int_to_binary(idade)
    sexo_bin = string_to_binary(sexo)

    data = nome_bin + idade_bin + sexo_bin
    total_bits = len(data)

    memoria = []
    for i in range(0, total_bits, 64):
        palavra = data[i:i+64].ljust(64, '0')
        memoria.append(palavra)

    matriz = []
    for i in range(0, len(memoria), 8):
        linha = memoria[i:i+8]
        matriz.append(linha)

    return matriz

# Função para imprimir a tabela de memória no formato Big Endian
def imprimir_memoria(matriz, endereco_inicial=6):
    endereco = endereco_inicial
    for linha in matriz:
        linha_str = f"{endereco};"
        for item in linha:
            linha_str += f"{item};"
        print(linha_str)
        endereco += 8

# Função corrigida para imprimir o conteúdo desconvertido da memória
def imprimir_memoria_desconvertida(matriz, endereco_inicial=6):
    tamanho_nome = len(string_to_binary("Denecley Alvim Soares"))  # 168 bits
    tamanho_idade = len(int_to_binary(36))  # 64 bits
    tamanho_sexo = len(string_to_binary("Masculino"))  # 72 bits

    print(f"Tamanho Nome: {tamanho_nome}, Tamanho Idade: {tamanho_idade}, Tamanho Sexo: {tamanho_sexo}")

    data = ""
    for linha in matriz:
        for palavra in linha:
            data += palavra

    nome_bin = data[:tamanho_nome]
    idade_bin = data[tamanho_nome:tamanho_nome + tamanho_idade]
    sexo_bin = data[tamanho_nome + tamanho_idade:tamanho_nome + tamanho_idade + tamanho_sexo]

    print(f"Nome binário: {nome_bin}")
    print(f"Idade binário: {idade_bin}")
    print(f"Sexo binário: {sexo_bin}")

    print(f"Tamanho de nome_bin: {len(nome_bin)}, idade_bin: {len(idade_bin)}, sexo_bin: {len(sexo_bin)}")

    if nome_bin and idade_bin and sexo_bin:
        nome_recuperado = binary_to_string(nome_bin)
        idade_recuperada = binary_to_int(idade_bin)
        sexo_recuperado = binary_to_string(sexo_bin)

        print("\nConteúdo da memória desconvertido de binário:")
        print(f"Nome: {nome_recuperado}")
        print(f"Idade: {idade_recuperada}")
        print(f"Sexo: {sexo_recuperado}")
    else:
        print("Erro: um ou mais campos estão vazios.")

# Dados fornecidos
nome = "Denecley Alvim Soares"
idade = 36
sexo = "Masculino"

# Gerar e imprimir a memória
matriz_memoria = gerar_memoria(nome, idade, sexo)
imprimir_memoria(matriz_memoria)
imprimir_memoria_desconvertida(matriz_memoria)
