# PyCodeBR Carros

Aplicação web desenvolvida com Django para cadastro, consulta e gerenciamento de veículos da PyCodeBR Multimarcas. O sistema oferece um catálogo público de carros, busca por modelo, upload de fotos e operações de gerenciamento protegidas por autenticação.

## Funcionalidades

- Listagem pública de veículos ordenada pelo modelo;
- busca de carros por nome do modelo;
- página de detalhes de cada veículo;
- cadastro, edição e exclusão de carros para usuários autenticados;
- cadastro, login e logout de usuários;
- associação de cada carro a uma marca;
- upload e exibição de fotos dos veículos;
- gerenciamento de marcas e carros pelo Django Admin;
- banco de dados SQLite para o ambiente local.

## Tecnologias

- Python 3.x;
- Django 6.1.1;
- SQLite;
- HTML e templates do Django;
- Pillow, usado pelo campo de imagem dos carros.

## Estrutura do projeto

```text
PyCode_BR_Carros/
├── app/                 # Configurações, URLs e templates compartilhados
├── accounts/            # Cadastro, login e logout de usuários
│   ├── templates/       # Telas de autenticação
│   └── views.py
├── cars/                # Domínio de marcas e veículos
│   ├── migrations/      # Migrações do banco de dados
│   ├── templates/       # Listagem, detalhes e CRUD de carros
│   ├── forms.py
│   ├── models.py
│   └── views.py
├── media/cars/          # Fotos enviadas pelos usuários
├── db.sqlite3           # Banco de dados local
├── manage.py            # Utilitário de administração do Django
└── README.md
```

## Modelos

### `Brand`

Representa a marca de um veículo.

- `name`: nome da marca.

### `Car`

Representa um veículo cadastrado.

- `model`: modelo do carro;
- `brand`: marca relacionada por chave estrangeira;
- `factory_year`: ano de fabricação;
- `model_year`: ano do modelo;
- `plate`: placa do veículo;
- `value`: valor do carro;
- `photo`: imagem armazenada em `media/cars/`.

Os campos de ano, placa, valor e foto podem ser deixados vazios. Uma marca não pode ser excluída enquanto estiver associada a carros.

## Rotas

| Rota | Acesso | Descrição |
| --- | --- | --- |
| `/cars/` | Público | Lista os carros e permite buscar por modelo usando `?search=`. |
| `/car/<id>/` | Público | Exibe os detalhes de um carro. |
| `/register/` | Público | Cria uma conta de usuário. |
| `/login/` | Público | Autentica um usuário. |
| `/logout/` | Autenticado | Encerra a sessão atual. |
| `/new_car/` | Autenticado | Cadastra um novo carro. |
| `/car/<id>/update/` | Autenticado | Edita um carro existente. |
| `/car/<id>/delete/` | Autenticado | Exclui um carro. |
| `/admin/` | Administrador | Acessa o painel administrativo do Django. |

## Requisitos

- Python 3.x;
- `pip`;
- ambiente virtual recomendado;
- dependências Django e Pillow.

## Instalação e execução

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd PyCode_BR_Carros
```

### 2. Crie e ative um ambiente virtual

No Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

No Linux/macOS:

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
python -m pip install django==6.1.1 pillow
```

### 4. Aplique as migrações

```bash
python manage.py migrate
```

### 5. Crie um usuário administrador (opcional)

```bash
python manage.py createsuperuser
```

### 6. Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

A aplicação ficará disponível em <http://127.0.0.1:8000/cars/>. O painel administrativo fica em <http://127.0.0.1:8000/admin/>.

## Desenvolvimento

Para verificar problemas de configuração antes de executar a aplicação:

```bash
python manage.py check
```

Para criar ou aplicar alterações futuras nos modelos:

```bash
python manage.py makemigrations
python manage.py migrate
```

Os arquivos enviados são servidos a partir de `media/` durante o desenvolvimento. O projeto está configurado com `DEBUG = True`, uma chave secreta de desenvolvimento e SQLite; essas configurações devem ser substituídas antes de qualquer implantação em produção.

## Testes

Execute a suíte de testes do Django com:

```bash
python manage.py test
```

Os arquivos de teste estão em `cars/tests.py` e `accounts/tests.py`. Novos fluxos e regras de negócio devem receber testes à medida que o projeto evoluir.

## Licença

Este projeto é destinado a estudo e desenvolvimento. Não há uma licença de distribuição definida no momento.
