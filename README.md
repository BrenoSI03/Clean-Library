# 📚 **Biblioteca Clean Architecture — Flask**

Este projeto implementa um **sistema de gerenciamento de biblioteca** utilizando **Python + Flask**, seguindo rigorosamente os princípios da **Clean Architecture**, **SOLID** e com **testes unitários via Pytest**.

O objetivo é demonstrar uma arquitetura desacoplada, sustentável e escalável, com casos de uso isolados da infraestrutura e repositórios que respeitam o princípio de inversão de dependência (DIP).

---

## 📌 **🎯 Objetivo do Projeto**

O sistema permite gerenciar uma biblioteca simples, incluindo:

* Cadastro de livros
* Listagem de livros
* Cadastro de usuários
* Empréstimo e devolução de livros

A aplicação foi construída com foco em:

* Estrutura limpa e organizada baseada em **Clean Architecture**
* Aplicação explícita dos princípios **SOLID**
* Testes unitários para **casos de uso**, isolando lógica de negócio da infraestrutura
* Uso de **Flask** como camada de interface web
* Persistência via **SQLite**

---

# 🏛 **🧱 Arquitetura do Projeto (Clean Architecture)**

A estrutura do projeto está organizada nas camadas:

```
project/
│
├── app/                     # Interface (Frameworks & Drivers)
│   ├── main.py              # Inicialização do Flask + DI
│   └── routes/              # Controladores e rotas HTTP
│
├── domain/                  # Regras essenciais de negócio (Entidades + Interfaces)
│   ├── entities/            # Entidades (Book, User)
│   └── repositories/        # Interfaces (Ports) dos Repositórios
│
├── use_cases/               # Casos de Uso (Application Business Rules)
│                            # Implementam regras de aplicação
│
├── infra/                   # Implementações concretas (Adapters)
│   ├── db/                  # Conexão SQLite
│   └── repositories/        # Implementação concreta dos repositórios
│
├── tests/                   # Testes unitários (pytest)
│   ├── domain/
│   └── use_cases/
│
├── requirements.txt         # Dependências
└── README.md
```

---

# 📂 **🧩 O que cada pasta faz**

### `app/`

Contém o Flask, rotas HTTP e ponto principal de execução.
**Função:** é a camada mais externa da arquitetura (frameworks & delivery).

---

### `domain/`

Contém o coração da aplicação.

* `entities/`: classes de domínio (Book, User)
* `repositories/`: interfaces que definem como a aplicação espera persistência

**Função:** independente de Flask, SQLite ou qualquer tecnologia.

---

### `use_cases/`

Implementa todas as regras de aplicação.

Exemplos:

* `add_book.py`
* `list_books.py`
* `loan_book.py`

**Função:** executam a lógica do sistema sem conhecer nada sobre bancos, web ou frameworks.

---

### `infra/`

Implementações concretas da infraestrutura — bancos, APIs, arquivos etc.

* Repositórios SQLite
* Banco de dados

**Função:** adaptar o mundo externo para o domínio.

---

### `tests/`

Contém testes unitários dos casos de uso e das entidades.

**Função:** garantir que a lógica de negócio funciona isolada da infraestrutura
(ex.: usando `unittest.mock`)

---

# 🚀 **🔧 Como rodar a aplicação**

### 1️⃣ Criar ambiente virtual (opcional, mas recomendado)

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 2️⃣ Instalar dependências

```
pip install -r requirements.txt
```

### 3️⃣ Inicializar banco de dados (se necessário)

Executa o script que cria as tabelas:

```
python infra/db/database.py
```

### 4️⃣ Rodar o Flask

```
python app/main.py
```

### 5️⃣ Abrir a aplicação no navegador

Acesse:

```
http://127.0.0.1:5000
```

Rotas disponíveis:

* `GET /books`
* `POST /books`
* `POST /users`
* `POST /loans/<book_id>`
* `POST /returns/<book_id>`

---

# 🧪 **🧷 Rodar os Testes (pytest)**

### 1️⃣ Executar todos os testes:

```
pytest
```

### 2️⃣ Mostrar testes com detalhes:

```
pytest -vv
```

### 3️⃣ Gerar relatório de cobertura (se quiser):

```
pytest --cov=use_cases --cov-report=term
```

---

# 📘 **📄 Tecnologias Utilizadas**

* Python 3.x
* Flask
* Pytest
* SQLite
* Clean Architecture
* SOLID

---