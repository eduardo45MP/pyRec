import os
from src.disk_reader.pytsk_interface import read_disk
from src.disk_reader.chunking import chunk_data
from src.disk_reader.preprocessing import preprocess_data
from src.aws_interaction.s3_storage import upload_to_s3
from src.aws_interaction.sagemaker_client import invoke_sagemaker_endpoint

def main():
    disk_path = '/dev/sda3'  # Altere conforme necessário
    bucket_name = 'recovery2'  # Altere para o nome do seu bucket S3
    endpoint_name = 'recovery-endpoint'  # Nome do seu endpoint do SageMaker

    # 1. Ler setores do disco
    sectors = read_disk(disk_path)
    print(f"Setores lidos: {sectors}")

    # 2. Pré-processar os setores
    processed_data = preprocess_data(sectors)
    print(f"Dados processados: {processed_data}")

    # 3. Dividir os dados em blocos
    chunk_size = 512  # Ajuste conforme necessário
    chunks = chunk_data(processed_data, chunk_size)
    
    # 4. Enviar cada bloco para o S3 e invocar o SageMaker
    for i, chunk in enumerate(chunks):
        # Salvar bloco em um arquivo temporário
        temp_file = f'temp_chunk_{i}.bin'
        with open(temp_file, 'wb') as f:
            f.write(chunk)
        
        # 5. Fazer upload para o S3
        upload_to_s3(bucket_name, temp_file)

        # 6. Invocar o SageMaker com os dados do bloco
        response = invoke_sagemaker_endpoint(endpoint_name, chunk)
        print(f"Resposta do SageMaker para o bloco {i}: {response}")

        # Remover arquivo temporário
        os.remove(temp_file)

if __name__ == "__main__":
    main()
