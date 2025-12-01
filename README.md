---

# ✅ **README.md atualizado**

# 📚 **Biblioteca Clean Architecture — Flask**

Este projeto implementa um **sistema de gerenciamento de biblioteca** utilizando **Python + Flask**, seguindo rigorosamente os princípios da **Clean Architecture**, **SOLID** e com **testes unitários via Pytest**.

O objetivo é demonstrar uma arquitetura desacoplada, sustentável e escalável, com casos de uso isolados da infraestrutura e repositórios que respeitam o princípio de inversão de dependência (DIP).

---

## 📌 **🎯 Objetivo do Projeto**

O sistema permite gerenciar uma biblioteca simples, incluindo:

- Cadastro de livros  
- Listagem de livros  
- Cadastro de usuários  
- Empréstimo e devolução de livros  

A aplicação foi construída com foco em:

- Estrutura limpa e organizada baseada em **Clean Architecture**
- Aplicação explícita dos princípios **SOLID**
- Testes unitários isolando a lógica de negócio
- Uso de **Flask** como camada web
- Persistência via **SQLite**

---

# 🏛 **🧱 Arquitetura do Projeto (Clean Architecture)**

Estrutura oficial do projeto:

```

clean-library/
│
├── app/                     # Interface (Frameworks & Drivers)
│   ├── main.py              # Inicialização do Flask + DI
│   ├── routes/              # Rotas HTTP
│   ├── templates/           # Templates HTML (Jinja2)
│   └── static/              # CSS, JS, imagens
│
├── domain/                  # Regras essenciais do negócio
│   ├── book.py              # Entidade Book
│   └── user.py              # Entidade User
│
├── repositories/            # Interfaces abstratas (Ports)
│   ├── book_repository.py
│   ├── user_repository.py
│   └── loan_repository.py
│
├── use_cases/               # Application Business Rules
│   ├── book/                # Casos de uso relacionados a livros
│   ├── user/                # Casos de uso relacionados a usuários
│   └── loan/                # Casos de uso relacionados a empréstimos
│
├── infra/                   # Implementações concretas (Adapters)
│   ├── db/
│   │   ├── database.py
│   │   └── init_db.py
│   └── repositories/        # Implementações SQLite
│
├── tests/                   # Testes unitários (pytest)
│   ├── domain/
│   └── use_cases/
│
├── requirements.txt
└── README.md

```

---

# 📂 **🧩 O que cada pasta faz**

## `app/`
Contém Flask, rotas e templates.
É a camada mais externa (interface web).

---

## `domain/`
Contém o núcleo do software: **as entidades**.

- `book.py`
- `user.py`

Não depende de nada externo.

---

## `repositories/`
Contém **interfaces abstratas** (ports) usadas pelos casos de uso:

- `BookRepository`
- `UserRepository`
- `LoanRepository`

Isso permite inversão de dependência (DIP).

---

## `use_cases/`
Implementa toda a **lógica de aplicação**, totalmente independente de Flask ou banco.

---

## `infra/`
Implementações concretas da infraestrutura:

- Conexão SQLite  
- Repositórios reais que implementam BookRepository, UserRepository e LoanRepository  

---

## `tests/`
Testes unitários:

- `tests/domain/`
- `tests/use_cases/`

Testes isolados, usando mocks (`unittest.mock`).

---

# 🚀 **🔧 Como rodar a aplicação**

## 1️⃣ Criar o ambiente virtual `.venv`

```

python -m venv .venv

```

Ativar:

**Windows:**
```

.venv\Scripts\activate

```

**Linux/macOS:**
```

source .venv/bin/activate

```

---

## 2️⃣ Instalar dependências

```

pip install -r requirements.txt

```

---

## 3️⃣ Inicializar o banco SQLite

```

python infra/db/init_db.py

```

---

## 4️⃣ Rodar a aplicação Flask

```

python -m app.main

```

Acesse no navegador:

```

http://127.0.0.1:5000

```

---

# 🧪 **🧷 Rodar os Testes (pytest)**

### Executar todos os testes:

```

pytest

```

### Mostrar detalhes:

```

pytest -vv

```

---

# 📘 **📄 Tecnologias Utilizadas**

- Python 3.x  
- Flask  
- Jinja2  
- Pytest  
- SQLite  
- Clean Architecture  
- SOLID  

---