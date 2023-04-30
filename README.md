# Prueba técnica validar alfabeto.
### Descripción del reto.
El objetivo de la función es recibir una cadena como entrada y validar si contiene todos los caracteres del alfabeto. La función debe de eliminar cualquier carácter que no esté en el alfabeto y luego verifica si todos los caracteres del alfabeto están presentes en la cadena limpia.
## Características.
-  Evaluar (la respuesta esperada es TRUE/FALSE) si en una misma cadena de texto están contenidos TODOS los caracteres del alfabeto EN ESPAÑOL (o sea, de la "a" a la "z" incluyendo "ñ" - mayúsculas o minúsculas).
- La cadena de texto a evaluar podría incluir números, caracteres especiales o no-alfabéticos (espacios,vocales acentuadas, # signos de puntuación, paréntesis, etc...), pero esos caracteres NO se incluyen en la lista de caracteres evaluados # Es decir: por sencillez, si la cadena contiene vocales acentuadas, esas se consideran caracteres especiales (para este caso, NO se consideran parte del alfabeto).
- El programa debe ser al menos funcional, y se debe poder evaluar cualquier cadena que se le ocurra al usuario.
- Proporcionar código fuente CON COMENTARIOS que expliquen la lógica aplicada y el modo de uso.
- Hay que referenciar fuentes (es válido usar código de terceros en tanto NO se presente como propio) en los mismos comentarios.
- Generar reporte de prueba del programa proporcionado, que incluya evidencia de resultados obtenidos y veredicto (PASA/FALLA) con conclusión razonada

## Cómo empezar.
Requiere [Python](https://www.python.org/).
#### Entorno virtual windows: 
```sh
python -m venv .venv
.\.venv\Scripts\activate
```
#### Entorno virtual MacOS:: 
```sh
python3 -m venv .venv
source .venv/bin/activate
```
#### Instala las dependencias
```sh
pip install -r requirements.txt
```
#### Correr test
```sh
pytest -v
```
## Funcionalidades.
#### Limpiar cadena
##### Objetivo:
El objetivo de la función "clean_string" es recibir una cadena como entrada y devolver un conjunto de todos los caracteres del alfabeto que están presentes en la cadena de entrada. Esta función es útil para filtrar los caracteres no deseados de una cadena y obtener solo los caracteres que son relevantes para una tarea en particular.

##### Entradas:
La función toma una entrada:
- words (str): Una cadena a evaluar.

##### Flujo:
La función primero crea un set vacío llamado "words_clean". Luego itera a través de cada carácter en la cadena de entrada, convirtiéndolo a minúsculas. Si el carácter está presente en la constante global "ALPHABET", se agrega al set "words_clean". Finalmente, la función devuelve el conjunto "palabra" que contiene todos los caracteres relevantes.
``` python
def clean_string(words:str):
	words_clean =set()
	for char in words.lower():
		if char in ALPHABET:
		words_clean.add(char)
	return words_clean
```

##### Salidas:
La función devuelve una salida:
- words_clean (conjunto): un conjunto de cadenas que contiene todos los caracteres del alfabeto que están presentes en la cadena de entrada.

##### Aspectos adicionales:
- La función utiliza una constante global "ALFABETO" que contiene todos los caracteres del alfabeto.
- La función convierte todos los caracteres de la cadena de entrada a minúsculas antes de evaluarlos.
- La función utiliza un set para almacenar los caracteres relevantes, asegurando que no haya duplicados en la salida.

#### Validar alfabeto 
##### Objetivo:
El objetivo de la función es recibir una cadena como entrada y validar si contiene todos los caracteres del alfabeto. La función usa una constante global para el alfabeto y una función auxiliar para limpiar la cadena de entrada antes de validarla.

##### Entradas:
La función toma una sola entrada, que es una cadena para ser evaluada. La entrada debe ser una cadena y, si no lo es, la función genera un TypeError.

##### Flujo:
La función primero verifica si la entrada es una cadena y genera un TypeError si no lo es. Luego, llama a la función auxiliar clean_string para limpiar la cadena de entrada y devolver un conjunto de todos los caracteres del alfabeto que están presentes en la cadena de entrada. Finalmente, la función verifica si todos los caracteres del alfabeto están presentes en la cadena de entrada limpia y devuelve True si lo están y False en caso contrario.
``` python
def validate_alphabet(words:str):
	if not isinstance(words, str):
		raise TypeError("Input must be a string")
	word_to_validate = clean_string(words)
	for char in ALPHABET:
		if char not in word_to_validate:
			return False
	return True
```

##### Salidas:
La función devuelve un valor booleano (Verdadero o Falso) que indica si la cadena de entrada contiene todos los caracteres del alfabeto.

##### Aspectos adicionales:
La función usa una constante global para el alfabeto, que se crea fuera de la función. La función también usa una función auxiliar, clean_string, para limpiar la cadena de entrada antes de validarla. La función clean_string devuelve un conjunto de todos los caracteres del alfabeto que están presentes en la cadena de entrada. La función no distingue entre mayúsculas y minúsculas, lo que significa que considera los caracteres en mayúsculas y minúsculas como iguales.
## Test
Se añadieron Test para verificar su correcto funcionamiento usando pytest.
[![2023-04-29-19-04-18-Cmder.png](https://i.postimg.cc/d1sWL8fq/2023-04-29-19-04-18-Cmder.png)](https://postimg.cc/wtr5rsHP)
### CI/CD
Asi mismo se añadieron los test a Github actions, para cada vez que se haga un push se corran las pruebas y asi no tengan que descargar los test.
[![aa.png](https://i.postimg.cc/1tXpkMTN/aa.png)](https://postimg.cc/MMkMR0zW)
## Tecnologías utilizadas
#### Codium
Se utilizó [Codium](https://www.codium.ai/) para que revisara las funciones creadas y proporcione un analisis de código, mismo que utilice para facilitar la documentación.
[![codium.png](https://i.postimg.cc/TPLbQhWr/codium.png)](https://postimg.cc/8FGszp45)
#### Github Actions
Se utilizó [Github Actions] (https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python) para generar test de integración continúa.
#### Pytest
Se utilizó [Pytest](https://docs.pytest.org/en/7.3.x/getting-started.html) para generar pruebas unitarias.
