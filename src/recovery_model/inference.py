import json
import numpy as np

# Modelo simples para detectar padrões de cabeçalhos de arquivos
def detect_file_type(data):
    signatures = {
        'png': b'\x89PNG',
        'jpg': b'\xFF\xD8\xFF',
        'pdf': b'%PDF'
    }

    for file_type, signature in signatures.items():
        if signature in data:
            return file_type
    return 'unknown'

# Função de processamento principal
def model_fn(model_dir):
    return None  # Para este exemplo, não treinamos nenhum modelo, apenas usamos detecção de padrões

# Função de inferência que será chamada no endpoint SageMaker
def input_fn(request_body, content_type='application/octet-stream'):
    if content_type == 'application/octet-stream':
        return request_body
    else:
        raise ValueError(f"Unsupported content type: {content_type}")

def predict_fn(input_data, model):
    # Processa o bloco de setores recebido
    file_type = detect_file_type(input_data)
    return {'file_type': file_type}

def output_fn(prediction, accept='application/json'):
    return json.dumps(prediction), accept