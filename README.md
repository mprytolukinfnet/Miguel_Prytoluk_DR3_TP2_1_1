# TP2 Exercício 1_1: Geração de Texto com GPT-2
Este aplicativo FastAPI utiliza o modelo GPT-2 da HuggingFace para gerar textos com base em uma entrada fornecida.

**Passos para Configuração**:

1. Certifique-se de que o ambiente Python está configurado.
2. Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```
3. Instalar Pytorch: https://pytorch.org/get-started/locally/

**Como Executar**: Inicie o servidor FastAPI com o comando:
```bash
uvicorn 1_1:app --reload
```

**Uso da API**: Faça uma requisição POST para gerar texto:

```bash
curl -X POST "http://127.0.0.1:8000/generate/" \
-H "Content-Type: application/json" \
-d '{"text": "Once upon a time"}'
```