# 🤖 WorkGuard AI

Sistema de monitoramento de segurança utilizando **visão computacional e inteligência artificial** para detectar pessoas e identificar quando alguém entra em uma área de risco.

O projeto foi desenvolvido em **Python**, utilizando **YOLO** para detecção de pessoas e **OpenCV** para processamento das imagens da câmera.

---

## 🎯 Objetivo

O WorkGuard AI foi criado como um protótipo de sistema de segurança capaz de monitorar uma área através de uma câmera.

Quando uma pessoa entra na área definida como perigosa, o sistema:

* 🔴 Identifica a pessoa
* 🚨 Gera um alerta visual
* 📸 Captura uma evidência
* 💾 Salva a ocorrência
* 🗄️ Registra informações no banco de dados
* 🔊 Pode utilizar um alerta sonoro

---

## 🧠 Como funciona

```text
📷 Câmera
   ↓
🧠 YOLO
   ↓
👤 Detecção de pessoa
   ↓
🔴 Verificação da área de risco
   ↓
🚨 Pessoa entrou na área?
   ↓
📸 Captura da ocorrência
   ↓
🗄️ SQLite
```

---

## 🚨 Área de risco

O sistema possui uma área definida na lateral da câmera.

Quando o centro da detecção de uma pessoa entra nessa região, o WorkGuard AI identifica a situação como um risco.

A interface mostra:

```text
WORKGUARD AI

Pessoas: 1

ALERTA: PESSOA NA AREA DE RISCO
```

---

## 📸 Captura de evidências

Quando uma pessoa entra na área de risco, o sistema pode capturar uma imagem da ocorrência.

As evidências são armazenadas localmente na pasta:

```text
salvos/
```

As imagens não são enviadas para o GitHub, pois essa pasta está protegida pelo `.gitignore`.

---

## 🗄️ Banco de dados

O projeto utiliza **SQLite** para armazenar informações relacionadas às ocorrências e às pessoas cadastradas.

Estrutura inicial:

```text
pessoas
├── id
├── nome
├── data_nascimento
├── cargo
└── foto

ocorrencias
├── id
├── data_hora
├── tipo
└── foto
```

---

## 🔊 Sistema de alerta

O projeto utiliza **Pygame** para trabalhar com áudio.

O arquivo:

```text
src/alarme.wav
```

pode ser utilizado para emitir um alerta sonoro quando uma situação de risco for identificada.

---

## 🛠️ Tecnologias

| Tecnologia | Utilização                        |
| ---------- | --------------------------------- |
| 🐍 Python  | Linguagem principal               |
| 🧠 YOLO    | Detecção de pessoas               |
| 👁️ OpenCV | Câmera e processamento de imagens |
| 🔊 Pygame  | Sistema de áudio                  |
| 🗄️ SQLite | Banco de dados                    |
| 🔧 Git     | Controle de versão                |
| ☁️ GitHub  | Hospedagem do código              |

---

## 📁 Estrutura do projeto

```text
workguard-AI/
│
├── src/
│   ├── main.py
│   ├── cadastro.py
│   ├── database.py
│   └── alarme.wav
│
├── models/
├── videos/
├── resultados/
├── salvos/
│
├── .gitignore
├── requirements.txt
├── yolo11n.pt
└── README.md
```

---

## ▶️ Como executar

### 1. Clone o projeto

```bash
git clone https://github.com/wanderley2002/workguard-AI.git
```

### 2. Entre na pasta

```bash
cd workguard-AI
```

### 3. Crie o ambiente virtual

Windows:

```bash
python -m venv .venv
```

### 4. Ative o ambiente

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute o sistema

```bash
python src/main.py
```

Uma janela será aberta utilizando a câmera do computador.

---

## 📌 Status do projeto

🚧 **Em desenvolvimento**

### Já implementado

* [x] Detecção de pessoas
* [x] Monitoramento da câmera
* [x] Área de risco
* [x] Identificação de situação de risco
* [x] Captura de evidências
* [x] Banco de dados SQLite
* [x] Cadastro de pessoas
* [x] Sistema de áudio
* [x] Versionamento com Git
* [x] Publicação no GitHub

### Próximas funcionalidades

* [ ] Reconhecimento facial
* [ ] Identificação da pessoa cadastrada
* [ ] Exibição do nome e cargo
* [ ] Registro automático das ocorrências
* [ ] Dashboard web
* [ ] Histórico de ocorrências
* [ ] Sistema de login
* [ ] Relatórios de segurança

---

## 👨‍💻 Desenvolvedor

**Wanderley Ariel**

Estudante de Análise e Desenvolvimento de Sistemas, desenvolvendo projetos com Python, JavaScript, inteligência artificial e visão computacional.

🔗 GitHub: https://github.com/wanderley2002

---

## ⚠️ Aviso

Este projeto é um **protótipo educacional** desenvolvido para estudo de inteligência artificial, visão computacional e desenvolvimento de sistemas.

Não deve ser utilizado como único mecanismo de segurança em ambientes reais sem validação, testes e adequações de segurança.
