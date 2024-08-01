import requests
import json

# Configuración
GITHUB_API_URL = 'https://api.github.com'
REPO_OWNER = 'Hades0413'  # Reemplaza con el propietario del repositorio
REPO_NAME = 'pr'  # Reemplaza con el nombre del repositorio
AUTH_TOKEN = 'tu_token_de_github'  # Reemplaza con tu token de GitHub

# Crear una función para crear un issue
def create_issue(title, body):
    url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    headers = {
        'Authorization': f'token {AUTH_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'title': title,
        'body': body
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 201:
        issue = response.json()
        print(f"Issue creado exitosamente.\nURL: {issue['html_url']}")
    else:
        print(f"Error al crear el issue.\nCódigo de estado: {response.status_code}\nRespuesta: {response.json()}")

# Crear issues
for i in range(1, 11):  # Cambia el rango según la cantidad de issues que quieras crear
    create_issue(f'Issue {i}', f'Este es el cuerpo del issue {i}.')
