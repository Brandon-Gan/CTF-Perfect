import requests
from prefect import flow, task


@task
def obtener_usuarios():
    respuesta = requests.get(
        "https://jsonplaceholder.cypress.io/users"
    )
    respuesta.raise_for_status()

    usuarios = respuesta.json()

    print(f"Usuarios obtenidos: {len(usuarios)}")

    return usuarios


@task
def obtener_publicaciones():
    respuesta = requests.get(
        "https://jsonplaceholder.cypress.io/posts"
    )
    respuesta.raise_for_status()

    publicaciones = respuesta.json()

    print(f"Publicaciones obtenidas: {len(publicaciones)}")

    return publicaciones


@task
def analizar_datos(usuarios, publicaciones):
    print("\n=== RESUMEN ===")
    print(f"Total de usuarios: {len(usuarios)}")
    print(f"Total de publicaciones: {len(publicaciones)}")

    publicaciones_por_usuario = {}

    for publicacion in publicaciones:
        usuario_id = publicacion["userId"]

        if usuario_id not in publicaciones_por_usuario:
            publicaciones_por_usuario[usuario_id] = 0

        publicaciones_por_usuario[usuario_id] += 1

    print("\nPublicaciones por usuario:")

    for usuario in usuarios:
        usuario_id = usuario["id"]
        nombre = usuario["name"]
        cantidad = publicaciones_por_usuario.get(usuario_id, 0)

        print(f"- {nombre}: {cantidad} publicaciones")


@flow
def analizar_jsonplaceholder():
    usuarios = obtener_usuarios()
    publicaciones = obtener_publicaciones()

    analizar_datos(usuarios, publicaciones)


if __name__ == "__main__":
    analizar_jsonplaceholder()