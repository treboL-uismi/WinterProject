<p aling="center">
    <img width="300" src="https://procomun.intef.es/files/articulos/guess_who_logo_side_es_b.jpg" alt="Logo QuienEsQuien">
</p>

<hr>

# **Winter Project - [¿Quién es quién?](https://es.wikipedia.org/wiki/Guess_Who%3F) Version 0.5.1**

# - *Contenidos básicos*
-   [**Introducción**](#introducción)
-   [**Manual**](#manual)
    -   [**Instalación**](#instalación)
-   [**Descripción Técnica**](#descripción-técnica)
    -   [**Diagrama de casos de uso**](#diagrama-de-casos-de-uso)
    -   [**Arquitectura de la aplicación**](#arquitectura-de-la-aplicación)
-   [**Implementacion**](#implementacion)
    -   [**Tecnologías y Herramientas Elegidas**](#tecnologías-y-herramientas-elegidas)
    -   [**Backend**](#backend)
    -   [**Frontend**](#frontend)
-   [**Casos Test**](#casos-test)
-   [**Comparación Temporal**](#comparación-temporal)
-   [**Conclusiones**](#conclusiones)
    -   [**Posibles mejoras**](#posibles-mejoras)
-   [**Dificultades**](#dificultades)

# **Introducción**
Proyecto de 1ºDAM hecho por Luis Miguel y Juan Pablo. Junto a otros compañeros del ciclo, tuvimos que crear un 
¿Quién es quién? con el framework open-source de **[Reflex](https://reflex.dev/)**.

# **Manual**
## **Instalación**
Para poder instalar este repositorio y acceder al juego, debemos primero crear la carpeta donde guardaremos el repo mediante:
```
mkdir ./nombre_app
cd ./nombre_app
```

Luego, debemos clonar el repositorio de GitHub
```
git clone https://github.com/treboL-uismi/WinterProject
```

Siguiente paso, debemos instalar un entorno virtual mediante esta otra cadena de comandos,

**Versión Linux**
```
python3 -m venv .venv
source .venv/bin/activate
```
**Versión Windows**
```
py -3 -m venv .venv
.venv\\Scripts\\activate
```

Por último, instalaremos las dependencias necesarias para poder acceder a la interfaz gráfica,
```
pip3 install -r requirements.txt
```

Si quisieramos iniciar la aplicación, tendríamos que hacer un ```reflex run```.

# **Descripción Técnica**
La aplicación basada en el Framework de Reflex, está obviamente inspirada en el juego de ¿Quién es quién?
Añade 2 modos de dificultad, el modo fácil y el difícil. Cada dificultad contiene diferentes cantidades de cartas o personajes, Modo Fácil (8), Modo Difícil (16).
## **Diagrama de casos de uso**

## **Arquitectura de la aplicación**
Proyecto dividido en varias carpetas,

*Miscelanea*
- /assets : Ubicación de las imágenes necesarias,

*Backend*
- /back/src : Ubicación de la lógica detrás de la aplicación,
- /back/test : Ubicación de los casos test,

*Frontend*
- /WinterProject : Carpeta fundamental para el funcionamiento de las páginas, aquí se guarda el "index" y la página de "New Game",
- /WinterProject/game_modes : Ubicación de los modos de dificultad,
- /WinterProject/start_Mode : Ubicación de las partidas.

# **Implementación**
## **Tecnologías y Herramientas Elegidas**
- [Reflex](https://reflex.dev/)
    - Framework escogido por nuestro Product Owner (nuestro profesor) para poder realizar el proyecto.
- [Python](https://www.python.org/)
    - [PIL](https://pypi.org/project/pillow/)
        - Librería escogida por Luismi para realizar un mapeado de imágenes con las tarjetas.
    - [Pytest](https://docs.pytest.org/en/stable/) + [Coverage](https://coverage.readthedocs.io/en/7.6.8/)
        - Librerías necesarias para realizar los casos test.

## **Backend**
## **Frontend**

# **Casos Test**


# **Comparación Temporal**


# **Conclusiones**
# **Posibles mejoras**

# **Dificultades**
