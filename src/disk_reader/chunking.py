def chunk_data(data, chunk_size):
    """
    Divide dados em blocos menores.

    :param data: Dados a serem divididos.
    :param chunk_size: Tamanho de cada bloco.
    :return: Lista de blocos.
    """
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

if __name__ == "__main__":
    # Exemplo de uso
    data = b"abcdefghijklmnopqrstuvwxyz"  # Exemplo de dados
    chunks = chunk_data(data, 5)
    print(f"Dados divididos em blocos: {chunks}")
