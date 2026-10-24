# 🪘 Além da Ginga

> Plataforma web full-stack desenvolvida para a gestão, divulgação e integração da comunidade de capoeira, unindo tradição cultural e inovação tecnológica.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0+-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Supabase](https://img.shields.io/badge/Supabase-PostgreSQL-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com/)
[![Cloudinary](https://img.shields.io/badge/Cloudinary-Media-3448C5?style=for-the-badge&logo=cloudinary&logoColor=white)](https://cloudinary.com/)
[![Render](https://img.shields.io/badge/Render-Backend-46E3B7?style=for-the-badge&logo=render&logoColor=black)](https://render.com/)
[![Vercel](https://img.shields.io/badge/Vercel-Frontend-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://vercel.com/)

---

## 📋 Sobre o Projeto

O **Além da Ginga** é um sistema web projetado para otimizar a organização de grupos de capoeira, gerenciamento de eventos (como o *Arena Além da Ginga*), publicação de conteúdos multimídia e engajamento da comunidade acadêmica e cultural. 

O projeto aplica boas práticas de engenharia de software, separação de responsabilidades (MVC/MVT do Django) e integração com serviços em nuvem modernos para persistência de dados, armazenamento de mídias e alta disponibilidade.

---

## ✨ Funcionalidades Principais

- **Gestão de Eventos & Inscrições:** Módulo dedicado para divulgação e controle de inscrições em eventos de capoeira, rodas e oficinas (incluindo suporte a materiais promocionais e QR codes).
- **Galeria Multimídia Otimizada:** Upload e gerenciamento dinâmico de fotos e vídeos dos treinos e apresentações via Cloudinary.
- **Painel Administrativo:** Interface customizada do Django Admin para controle seguro de usuários, permissões e conteúdos.
- **Design Responsivo:** Interface limpa e adaptada para dispositivos móveis e desktops utilizando HTML5, CSS3 (Flexbox/Grid) e JavaScript.

---

## 🛠️ Tecnologias Utilizadas

### **Backend & Core**
- **Python 3.11+**
- **Django Framework** (Django ORM, Authentication, Migrations)
- **Gunicorn** (Servidor WSGI para produção)

### **Banco de Dados & Armazenamento**
- **PostgreSQL** (Hospedado no [Supabase](https://supabase.com/))
- **Cloudinary** (Armazenamento e otimização de mídias em nuvem)

### **Frontend**
- **HTML5 & CSS3** (Com variáveis customizadas, Flexbox e Grid)
- **JavaScript (ES6+)**
- **Font Awesome** (Ícones)

### **Deploy & Infraestrutura**
- **Render** (Hospedagem do Backend/Aplicação Django)
- **Vercel / UFPA Server** (Hospedagem de recursos estáticos e frontend)
- **Git & GitHub** (Controle de versão)

---

## 📂 Arquitetura do Projeto

```text
alemdaginga/
├── core/                  # App principal do Django (Views, Models, Forms)
├── alemdaginga/           # Configurações do projeto Django (settings, urls, wsgi)
├── static/                # Arquivos estáticos (CSS, JavaScript, imagens locais)
├── templates/             # Templates HTML responsivos
├── media/                 # Gerenciamento temporário / integração Cloudinary
├── requirements.txt       # Dependências do projeto Python
├── manage.py              # CLI do Django
└── README.md              # Documentação do projeto