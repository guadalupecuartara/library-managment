import urllib.request  # Importamos el módulo que nos permite hacer solicitudes HTTP
import json  # Importamos el módulo que nos permite trabajar con datos en formato JSON
import textwrap  # Importamos el módulo que nos permite dar formato a la sinopsis


def agregador(codigo):
    # Definimos la URL base para hacer la solicitud a la API de Google Books
    base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

    with urllib.request.urlopen(base_api_link + codigo) as url:
        text = url.read()

    # Decodificamos la respuesta en formato JSON
    decoded_text = text.decode("utf-8")
    libro = json.loads(decoded_text)

    # Comprobamos si la respuesta de la API tiene información sobre el libro
    if libro.get("items") is None:
        return "No se encontro el libro"
    else:
        libro_data = libro["items"][0]
        # Extraemos los datos relevantes del libro, como el título, la sinopsis, el autor y el género
        # Si no hay autores, ponemos "No disponible"
        autores = libro_data["volumeInfo"].get("authors", ["No disponible"])
        # Si no hay título, ponemos "No disponible"
        titulo = libro_data["volumeInfo"].get("title", "No disponible")
        # Si no hay sinopsis, ponemos "No disponible"
        sinopsis = libro_data["volumeInfo"].get("description", "No disponible")
        # Formateamos la sinopsis a un ancho de 65 caracteres por línea
        sinopsis = textwrap.fill(sinopsis, width=65)
        autor = autores[0]  # Tomamos solo el primer autor, si hay varios
        genero = libro_data["volumeInfo"].get("categories", ["No disponible"])[
            0]  # Si no hay género, ponemos "No disponible"
    return {"titulo": titulo, "autor": autor, "genero": genero, "sinopsis": sinopsis}
