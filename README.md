# 🗂️ pyRec – Python Recovery & Analysis Toolkit

**pyRec** é um sistema em Python para **leitura, recuperação e análise de dados** com suporte a **modelos de IA** e integração com a **AWS (S3 e SageMaker)**.
Ele combina módulos de processamento local (discos, chunking, pré-processamento) com pipelines de inferência em nuvem para criar um fluxo robusto de extração e análise.

---

## 🚀 Funcionalidades
- 📡 **Integração com AWS**
  - Upload/download para S3.
  - Clientes para SageMaker (inferência e deploy de modelos).
- 💾 **Leitura e Recuperação de Disco**
  - Chunking e pré-processamento de dados binários.
  - Integração com `pytsk` para leitura de sistemas de arquivos.
- 🧠 **Modelos de Recuperação**
  - Pipeline de inferência local (`inference.py`).
  - Modelo já empacotado em `model.tar.gz`.
- 📝 **Logging & Config**
  - Configurações centralizadas (`config.py`).
  - Logger customizado (`logger.py`).
- 🔧 **Orquestração**
  - `main.py` coordena leitura, processamento e inferência.

---

## 📂 Estrutura do Projeto
```

pyRec/
├── main.py                  # Ponto de entrada principal
├── requirements.txt         # Dependências
├── src/
│   ├── aws_interaction/     # Integração AWS (S3, SageMaker)
│   ├── disk_reader/         # Leitura e chunking de discos
│   ├── recovery_model/      # Inferência e modelo pré-treinado
│   ├── utils/               # Config e logger
│   └── endpointTester.py    # Testes de endpoints
├── data/processed/          # Dados processados
├── logs/                    # Logs de execução
└── temp_chunk_0.bin         # Exemplo de chunk gerado

````

---

## ⚙️ Tecnologias
- **Python 3.12+**
- **AWS SDK (boto3)** para S3 e SageMaker.
- **pytsk3** para leitura de discos.
- **NumPy, Pandas** para processamento.
- **Scikit-learn / PyTorch** (dependendo do modelo em `model.tar.gz`).

---

## ▶️ Como Rodar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/pyRec.git
cd pyRec
````

2. Crie o ambiente virtual e instale as dependências:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Execute o pipeline principal:

```bash
python main.py
```

---

## 📑 Casos de Uso

* 🔍 Recuperação de dados de discos formatados ou corrompidos.
* 🧠 Inferência com modelos de IA treinados em AWS SageMaker.
* ☁️ Integração com pipelines em nuvem para análise massiva de dados.

---

## 📜 Licença

MIT – livre para uso e modificação.

---

✨ Criado por **Eduardo45MP.dev** como repositório aberto de estudos em **recuperação de dados e análise com IA**.
