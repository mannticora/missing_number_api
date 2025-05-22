
## 📘 API Numero Faltante 

### Descripción

**Missing Number API** es una aplicación web desarrollada con **Python 3.11** y **Flask**, que permite simular la extracción de un número del conjunto de los primeros 100 números naturales y calcular cuál fue el número faltante.

Este proyecto se desarrolló como parte de una prueba técnica para demostrar habilidades en diseño de lógica, desarrollo de APIs y validación de datos.

---

### 🚀 Funcionalidad

La API expone un endpoint que:

1. Recibe un número del 1 al 100.
2. Simula su extracción del conjunto completo.
3. Calcula y devuelve el número faltante (es decir, el número que se extrajo).

---

### 🛠 Tecnologías utilizadas

* 🐍 **Python 3.11**
* 🌐 **Flask 2.3.2** (framework para crear APIs REST)
* 🧪 Postman o cURL (para pruebas)
* 💻 IntelliJ IDEA (o cualquier editor compatible)

---

### 📂 Estructura del proyecto

```
missing_number_api/
├── app.py               # Archivo principal de la API
├── number_set.py        # Lógica de negocio (clase NumberSet100)
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación
```

---

### ⚙️ Instalación y ejecución

1. Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/missing-number-api.git
cd missing-number-api
```

2. (Opcional) Crea y activa un entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate  # En Windows
source venv/bin/activate  # En Linux/Mac
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecuta la aplicación:

```bash
python app.py
```

La API quedará disponible en:
📍 `http://127.0.0.1:5000/api/extract`

---

### 🧪 Ejemplo de uso

#### Endpoint: `POST /api/extract`

**Body** (formato JSON):

```json
{
  "number": 42
}
```

**Respuesta**:

```json
{
  "numero_extraido": 42
}
```

---

### 🔒 Validaciones

* Solo se aceptan números enteros entre 1 y 100.
* Si el número ya ha sido extraído o está fuera de rango, se retorna un error.

---

### 💡 Recomendaciones

* Ejecuta la API dentro de un entorno virtual para evitar conflictos con otras bibliotecas.
* Puedes probar la API usando herramientas como **Postman**, **Insomnia** o desde terminal con `curl`.
* Esta API puede extenderse para llevar un historial de múltiples extracciones y operaciones más complejas.

---

### 📜 Licencia

Este proyecto se entrega para fines educativos y técnicos. Puedes modificarlo y adaptarlo según tus necesidades.

---
