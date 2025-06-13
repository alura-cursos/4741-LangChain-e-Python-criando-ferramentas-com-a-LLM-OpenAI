<img width="989" alt="image" src="https://github.com/user-attachments/assets/c140d5f9-a165-44d0-80b9-592fdbf16e03" />


# LangChain e Python: criando ferramentas com a LLM OpenAI

## ⚙️ Guia de Configuração

Siga os passos abaixo para configurar seu ambiente e utilizar os scripts do projeto.

### 1. Criar e Ativar Ambiente Virtual

**Windows:**
```bash
python -m venv langchain
langchain\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv langchain
source langchain/bin/activate
```

### 2. Instalar Dependências

Utilize o comando abaixo para instalar as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

### 3. Configurar Chave da OpenAI

Crie ou edite o arquivo `.env` adicionando sua chave de API da OpenAI:
```bash
OPENAI_API_KEY="SUA_CHAVE_DE_API"
```
