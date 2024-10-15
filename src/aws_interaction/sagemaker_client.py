import boto3

def invoke_sagemaker_endpoint(endpoint_name, payload):
    """
    Invoca um endpoint do SageMaker.

    :param endpoint_name: Nome do endpoint do SageMaker.
    :param payload: Dados a serem enviados para o endpoint.
    :return: Resposta do SageMaker.
    """
    sagemaker_client = boto3.client('sagemaker-runtime')

    try:
        response = sagemaker_client.invoke_endpoint(
            EndpointName=endpoint_name,
            ContentType='application/json',  # Ajuste conforme necessário
            Body=payload
        )
        return response['Body'].read()
    except Exception as e:
        print(f"Erro ao invocar o endpoint do SageMaker: {e}")
        return None

if __name__ == "__main__":
    # Exemplo de uso
    endpoint_name = 'recovery-endpoint'
    sample_payload = '{"data": "exemplo de dados"}'  # Ajuste conforme o esperado pelo seu modelo
    response = invoke_sagemaker_endpoint(endpoint_name, sample_payload)
    print(f"Resposta do SageMaker: {response}")
