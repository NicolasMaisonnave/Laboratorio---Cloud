## ⚙️ Requisitos

- **Node.js** (v18+)
- **Python 3.12** (o compatible con tu entorno)
- **Azure Functions Core Tools**  
  ```bash
  npm install -g azure-functions-core-tools@4 --unsafe-perm true

  VSCode (opcional, recomendado)

Extensión Live Server (para el frontend)

Paquetes Python:

pip install -r api/requirements.txt

💻 Ejecución
1. Backend (Azure Functions)

Entrar a la carpeta del backend:

cd Laboratorio1/api


Activar el entorno virtual:

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate


Instalar dependencias:

pip install -r requirements.txt


Levantar Azure Functions (habilitando CORS para el frontend):

func start --cors "http://localhost:5500"


⚠ Para pruebas rápidas, también se puede usar --cors "*".

2. Frontend

Entrar a la carpeta frontend:

cd ../frontend


Abrir index.html con Live Server en VSCode:

Click derecho → Open with Live Server

Debe abrirse algo como: http://localhost:5500/index.html

Usar el portal para agregar y ver noticias.
