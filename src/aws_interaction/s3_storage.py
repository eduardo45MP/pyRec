import boto3
import os

def upload_to_s3(bucket_name, file_name, object_name=None):
    """
    Faz upload de um arquivo para um bucket S3.

    :param bucket_name: Nome do bucket S3.
    :param file_name: Caminho do arquivo local a ser enviado.
    :param object_name: Nome do objeto S3. Se None, file_name será usado.
    """
    if object_name is None:
        object_name = os.path.basename(file_name)

    s3_client = boto3.client('s3')
    
    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
        print(f"Arquivo {file_name} enviado para {bucket_name}/{object_name}.")
    except Exception as e:
        print(f"Erro ao enviar para S3: {e}")

if __name__ == "__main__":
    # Exemplo de uso
    upload_to_s3('recovery2', 'arquivo.txt')
