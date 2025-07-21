# Tasker 🗂️ ✅

Tasker é uma aplicação web desenvolvida com Django para gerenciamento de projetos e tarefas, com controle de usuários e permissões. Este projeto foi criado como avaliação individual da disciplina de Desenvolvimento Web.

## 📋 Funcionalidades

- Autenticação de usuários (login, logout, registro)
- CRUD completo de usuários (restrito ao administrador)
- CRUD de projetos (criação, listagem, edição, exclusão)
- CRUD de tarefas (vinculadas à projetos - 1:N - )
- Controle de permissões (usuários comuns vs. superusuários)
- Interface responsiva com Bootstrap 5

## 🔐 Requisitos de autenticação

- Apenas usuários autenticados podem acessar o sistema
- Superusuários podem gerenciar todos os usuários
- Usuários comuns podem editar apenas seus próprios dados e senha

## ⚙️ Tecnologias utilizadas

- Python 3.13+
- Django 5.2+
- Bootstrap 5 (via CDN)
- Function-Based Views (FBV)
- SQLite3 (banco de dados padrão)

## 🛠️ Instalação e execução

1. Clone o repositório:
```bash
git clone https://github.com/diogosilveiradev/Tasker
cd Tasker
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Aplique as migrações:
```bash
python manage.py migrate
```

5. Crie um superusuário:
```bash
python manage.py createsuperuser
```

6. Rode o servidor:
```bash
python manage.py runserver
```

Acesse o sistema em [http://127.0.0.1:8000]

## 🎥 Apresentação em vídeo

👉 [Clique aqui para assistir à demonstração do sistema](https://youtu.be/xa_SE7yxZvg)

## 📁 Organização do projeto

- `usuarios/`: gerenciamento de contas e permissões
- `projetos/`: funcionalidades de criação e controle de projetos
- `tarefas/`: gerenciamento de tarefas ligadas a projetos
- `templates/`: arquivos HTML com uso de Bootstrap
- `Tasker/`: configurações principais do projeto

---

Desenvolvido por Diôgo Ribeiro Silveira
