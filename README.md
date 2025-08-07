
# 🕹️ Hollow Knight Wiki — Projeto WebDesign

Este repositório contém o desenvolvimento de um projeto acadêmico de WebDesign, cujo objetivo é criar um site tipo "wiki" sobre o jogo **Hollow Knight**, utilizando o framework **Django** como backend e HTML/CSS com apoio de **Bootstrap** no frontend.

---

## 📄 Índice

- [🎯 Objetivo](#-objetivo)
- [🧠 Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [📐 Estrutura do Projeto](#-estrutura-do-projeto)
- [🌐 Rotas do Site](#-rotas-do-site)
- [📷 Layout e Wireframes](#-layout-e-wireframes)
- [⚙️ Como Executar](#-como-executar)
- [📌 Funcionalidades](#-funcionalidades)
- [📚 Conteúdo](#-conteúdo)
- [⚠️ Avisos Legais](#️-avisos-legais)

---

## 🎯 Objetivo

Desenvolver um site informativo e visualmente organizado que sirva como uma wiki para o jogo **Hollow Knight**, contendo informações sobre o mundo do jogo, personagens, itens, feitiços, chefes e mais — com foco em experiência do usuário e boas práticas de Web Design.

---

## 🧠 Tecnologias Utilizadas

- **Backend:** Django 4.x
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Design de interface:** Figma
- **Versionamento:** Git + GitHub
- **Imagens e ícones:** Assets do jogo Hollow Knight

---

## 📐 Estrutura do Projeto

```
/webdesign_trabalho_engine/
│
├── core/                  # App principal com as páginas
├── static/                # CSS, JS, imagens
│   ├── css/
│   └── img/
├── templates/             # Templates HTML das páginas
├── manage.py              # Script principal Django
├── requirements.txt       # Dependências do projeto
└── README.md              # Este arquivo
```

---

## 🌐 Rotas do Site

As rotas disponíveis no projeto são:

| Página                 | URL            | Descrição                                               |
|------------------------|----------------|----------------------------------------------------------|
| Página inicial         | `/`            | Landing page com introdução, objetivo e destaques        |
| Mundo                  | `/mundo`       | História, personagens e ambientação do jogo              |
| Itens e Habilidades    | `/itens`       | Amuletos, máscaras, feitiços, skills e artes do ferrão   |
| Exploração             | `/exploracao`  | Regiões, interações e locais especiais                   |
| Inimigos e Chefes      | `/inimigos`    | Chefes principais, mini-chefes e inimigos comuns         |

---

## 📷 Layout e Wireframes

O layout e o fluxo do site foram projetados no Figma antes do desenvolvimento.

🔗 [Visualizar wireframe no Figma](https://www.figma.com/design/0wp0fUqoHksAeCDTFkCjrv/WebDesign---Wireframe-Fandom?node-id=0-1&t=OfjX8udqV08OwnxE-0) <!-- Substitua com o link real quando publicar -->

---

## ⚙️ Como Executar

1. **Clone o repositório**:

```bash
git clone --branch master https://github.com/keventapi/webdesign_trabalho_engine.git
cd webdesign_trabalho_engine
```

2. **Crie um ambiente virtual e ative**:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**:

```bash
pip install -r requirements.txt
```

4. **Execute o servidor**:

```bash
python manage.py runserver
```

5. **Acesse no navegador**:

```
http://localhost:8000/
```

---

## 📌 Funcionalidades

- ✅ Página inicial com introdução e destaques
- ✅ Navegação clara entre as sessões
- ✅ Seções organizadas: Mundo, Itens e Habilidades, Exploração, Inimigos e Chefes
- ✅ Layout responsivo com Bootstrap
- ✅ Carrosséis, tabelas e cards interativos
- ✅ Estrutura escalável com Django

---

## 📚 Conteúdo

As principais seções do site incluem:

- **Mundo:** História, personagens e ambientação de Hallownest
- **Itens e Habilidades:** Amuletos, feitiços, máscaras, vessels e mais
- **Exploração:** Regiões, interações e locais especiais
- **Inimigos e Chefes:** Mini-chefes, chefes principais e inimigos comuns

---

## ⚠️ Avisos Legais

> Este é um projeto **não oficial** e **sem fins lucrativos**.  
> Todos os direitos sobre o jogo Hollow Knight pertencem à **Team Cherry**.  
> Imagens, nomes e referências são utilizados com propósito educacional e demonstrativo.

---
