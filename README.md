# api-qa-automation-framework
# API QA Automation Framework

Framework de pruebas automatizadas para validación de APIs REST, desarrollado con Python y Postman. El proyecto demuestra un enfoque de doble capa: diseño visual de casos de prueba en Postman y replicación programática con Python para integración en pipelines de CI/CD.

---

## 🛠️ Tecnologías y Herramientas

| Herramienta | Uso |

| Python 3.x | Lenguaje principal de automatización |
| `unittest` | Framework de pruebas estándar |
| `requests` | Consumo y validación de APIs REST |
| Postman | Diseño y ejecución visual de colecciones |
| Git / GitHub | Control de versiones |

---

## 🎯 Objetivo del Proyecto

Validar el comportamiento de endpoints REST públicos (JSONPlaceholder) mediante la automatización de casos de prueba que cubren flujos exitosos y escenarios de error, asegurando la integridad de respuestas JSON, códigos de estado HTTP y estructura de datos.


## 📁 Estructura del Repositorio

```
api-qa-automation-framework/
│
├── test_api_reqres.py                        # Suite de pruebas automatizadas en Python (unittest)
├── JSONPlaceholder API QA.postman_collection.json  # Colección de pruebas en Postman
└── README.md
```

---

## ✅ Casos de Prueba Cubiertos

### Suite Python (`test_api_reqres.py`)

| # | Caso de Prueba | Método | Endpoint | Validación |
|---|---|---|---|---|
| 1 | Creación exitosa de recurso | `POST` | `/posts` | Status `201 Created`, ID generado, título correcto en respuesta |
| 2 | Recurso inexistente | `GET` | `/endpoint_invalido` | Status `404 Not Found` |

### Colección Postman (`JSONPlaceholder API QA`)

- Pruebas sobre endpoints de JSONPlaceholder con scripts de validación en JavaScript
- Verificación de estructuras JSON y códigos de estado HTTP

---

## ▶️ Cómo Ejecutar las Pruebas

### Prerrequisitos

```bash
pip install requests
```

### Ejecución

```bash
python -m unittest test_api_reqres.py -v
```

### Resultado esperado

```
test_crear_publicacion_exitosa ... ok
test_recurso_no_encontrado ... ok

----------------------------------------------------------------------
Ran 2 tests in X.XXXs

OK
```

---

## Conceptos de QA Aplicados

- **Happy Path Testing** — validación del flujo exitoso con datos correctos
- **Negative Testing** — verificación del comportamiento ante entradas inválidas
- **Validación de contratos REST** — verificación de códigos de estado HTTP estándar (`201`, `404`)
- **Assertions sobre estructura JSON** — validación de campos y valores en la respuesta
- **Doble cobertura** — mismo caso de prueba ejecutado en Postman y Python para mayor confiabilidad

---

##  Autora

**Valeria** — [github.com/valee26](https://github.com/valee26)
