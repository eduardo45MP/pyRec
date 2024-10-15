import boto3

def send_data_to_sagemaker(endpoint_name, data_chunk):
    client = boto3.client('sagemaker-runtime')

    # Invocar o endpoint do SageMaker
    response = client.invoke_endpoint(
        EndpointName=endpoint_name,
        Body=data_chunk,
        ContentType='application/octet-stream'
    )

    result = response['Body'].read()
    return result

if __name__ == '__main__':
    endpoint_name = 'recovery-endpoint'

    # Dados simulados (substitua pelo resultado da leitura do HD)
    data_chunk = b'\x89PNG'  # Simulando um pedaço de setor com assinatura PNG

    # Enviar dados para o SageMaker e receber a resposta
    result = send_data_to_sagemaker(endpoint_name, data_chunk)
    print(f"Resultado do SageMaker: {result}")
