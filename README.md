# Carros

Aplicação web desenvolvida em Django para gerenciar uma base de carros, com listagem de veículos em uma interface simples.

## Visão geral

Este projeto foi criado para demonstrar o uso de Django em um cenário prático de cadastro e consulta de automóveis. A aplicação possui:

- modelagem de marcas e veículos;
- relacionamento entre `Brand` e `Car`;
- upload de fotos dos veículos;
- listagem dos carros em uma página HTML;
- uso do SQLite como banco de dados local.

## Tecnologias utilizadas

- Python
- Django
- SQLite
- HTML
- Pillow (para imagens)

## Estrutura do projeto

```text
Carros/
├── app/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── cars/
│   ├── migrations/
│   ├── templates/
│   │   └── cars.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── media/
│   └── cars/
├── db.sqlite3
├── manage.py
├── README.md
├── venv/
└── .gitignore
```

## Modelos principais

### Brand

Representa a marca do carro, com os seguintes campos:

- `id`
- `name`

### Car

Representa o veículo, com os seguintes campos:

- `id`
- `model`
- `brand` (chave estrangeira para `Brand`)
- `factory_year`
- `model_year`
- `plate`
- `value`
- `photo`

## Funcionalidades

- Cadastro de marcas e carros via Django ORM;
- listagem de todos os carros em uma página;
- associação de cada carro a uma marca;
- armazenamento de imagens em `media/cars/`;
- acesso à rota `/cars/` para visualizar os veículos.

## Requisitos

Antes de iniciar, verifique se você tem instalado:

- Python 3.x
- pip
- virtualenv (opcional, mas recomendado)

## Como executar

### 1. Clone o projeto

```bash
git clone <url-do-repositorio>
cd Carros
```

### 2. Crie e ative um ambiente virtual

Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install django pillow
```

### 4. Execute as migrações

```bash
python manage.py migrate
```

### 5. Inicie o servidor

```bash
python manage.py runserver
```

Acesse no navegador:

```text
http://127.0.0.1:8000/cars/
```

## Rotas principais

- `/admin/` — painel administrativo do Django
- `/cars/` — listagem de carros

## Observações

- O projeto usa o SQLite por padrão, o que facilita execução local e testes iniciais.
- Os arquivos de mídia ficam na pasta `media/`.
- O projeto está em um estágio inicial de desenvolvimento e pode ser expandido com cadastro, edição, exclusão e sistema de autenticação.

## Próximos passos sugeridos

- criar views para cadastro de carros;
- criar formulários com Django Forms;
- implementar edição e exclusão de registros;
- adicionar autenticação de usuários;
- melhorar a interface frontend com Bootstrap ou outro framework CSS.

## Licença

Este projeto é um exemplo acadêmico e de estudo, sem licença específica definida.
