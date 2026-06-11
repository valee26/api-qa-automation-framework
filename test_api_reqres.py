import unittest
import requests

class TestJsonPlaceholderAPI(unittest.TestCase):
    
    def setUp(self):
        # Cambiamos a una API que no requiere API Keys en 2026
        self.base_url = "https://jsonplaceholder.typicode.com"
        self.headers = {
            "Content-Type": "application/json; charset=UTF-8"
        }

    # PRUEBA 1: Validar la creación exitosa de un recurso (POST)
    def test_crear_publicacion_exitosa(self):
        url = f"{self.base_url}/posts"
        payload = {
            "title": "Prueba de QA Automatizada",
            "body": "Validando el endpoint con Python Requests",
            "userId": 1
        }
        
        response = requests.post(url, json=payload, headers=self.headers)
        
        # --- ASERCIONES DE QA ---
        # En metodologías REST, una creación exitosa regresa un código 201 Created
        self.assertEqual(response.status_code, 201, "El código de estado debería ser 201")
        
        response_json = response.json()
        # Validamos que el servidor nos regrese el objeto con un ID asignado
        self.assertIn("id", response_json, "La respuesta no generó un ID para el recurso")
        self.assertEqual(response_json["title"], "Prueba de QA Automatizada")

    # PRUEBA 2: Validar la respuesta correcta ante un recurso que no existe (404)
    def test_recurso_no_encontrado(self):
        # Forzamos un endpoint que no existe agregando texto inválido
        url = f"{self.base_url}/endpoint_invalido_de_prueba"
        
        response = requests.get(url, headers=self.headers)
        
        # --- ASERCIONES DE QA ---
        # Debe regresar un código 404 Not Found
        self.assertEqual(response.status_code, 404, "Debería retornar un código 404 para un recurso inexistente")

if __name__ == "__main__":
    unittest.main(verbosity=2)