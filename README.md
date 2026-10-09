# Além da Ginga 🪘

Uma aplicação web desenvolvida em Python para gestão e geração de páginas estáticas/dinâmicas para o projeto **Além da Ginga**. O sistema conta com um painel de administração para edição de conteúdo e um serviço dedicado para geração de ficheiros HTML.

## 🗂️ Estrutura do Projeto

```
alemdaginga/
├── app/
│   ├── routes/
│   │   └── posts.py          # Rotas para gestão de posts/publicações
│   ├── services/
│   │   └── geradorHTML.py    # Serviço responsável pela compilação/geração do HTML
│   └── main.py               # Ponto de entrada da aplicação backend
├── public/
│   ├── css/
│   │   ├── eventos.css       # Estilos específicos da página de eventos
│   │   ├── index.css         # Estilos da página principal
│   │   ├── sobre.css         # Estilos da página "Sobre"
│   │   └── template.css      # Estilos base para os templates
│   ├── img/                  # Recursos de imagem do site
│   ├── js/
│   │   └── carousel.js       # Script do carrossel/slider interativo
│   └── posts/
│       ├── eventos-index.html # Página final de listagem de eventos
│       ├── index.html        # Página principal pública
│       └── sobre.html        # Página institucional "Sobre"
├── templates/
│   ├── admin/
│   │   ├── editor.html       # Interface visual do editor de conteúdo
│   │   └── login.html        # Página de autenticação do administrador
│   └── template.html         # Modelo base HTML para renderização
├── .env                      # Variáveis de ambiente
└── README.md                 # Documentação do projeto

```

## 🚀 Funcionalidades

* **Painel Administrativo (`/templates/admin`)**:

  * Autenticação de utilizadores (`login.html`).

  * Editor visual para criação e modificação de publicações (`editor.html`).

* **Gerador de HTML (`app/services/geradorHTML.py`)**:

  * Transforma os dados ou publicações criadas em páginas HTML estáticas e otimizadas na pasta `public/`.

* **Interface Pública (`/public`)**:

  * Exibição da página inicial, eventos e secção institucional "Sobre".

  * Carrossel dinâmico em JavaScript (`carousel.js`).

  * Estilização modular com ficheiros CSS dedicados.

## 🛠️ Tecnologias Utilizadas

* **Backend**: Python (Framework web como FastAPI, Flask ou similar)

* **Frontend**: HTML5, CSS3, JavaScript (ES6+)

* **Modelagem**: Jinja2 / HTML Templates

* **Configuração**: Variables de ambiente (`.env`)

## ⚙️ Configuração e Instalação

### Pré-requisitos

* **Python 3.8+** instalado.

### 1. Clonar o repositório

```
git clone https://github.com/teu-usuario/alemdaginga.git
cd alemdaginga

```

### 2. Criar e ativar um ambiente virtual

```
# No Linux/macOS:
python3 -m venv venv
source venv/bin/activate

# No Windows:
python -m venv venv
venv\Scripts\activate

```

### 3. Instalar as dependências

```
pip install -r requirements.txt

```

*(Nota: Certifica-te de criar o ficheiro `requirements.txt` com as tuas bibliotecas Python).*

### 4. Configurar as variáveis de ambiente

Cria/edita o ficheiro `.env` na raiz do projeto seguindo este modelo:

```
PORT=8000
SECRET_KEY=sua_chave_secreta_aqui
DEBUG=True

```

### 5. Executar a aplicação

```
python app/main.py

```

Acede à aplicação através do teu navegador em: `http://localhost:8000`

## 📝 Licença

Este projeto está sob a licença [MIT](LICENSE).