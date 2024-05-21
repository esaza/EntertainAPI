# Creamos la clase principal de la API
class PrincipalAPI:

    # Método para la ruta principal de la API
    def hola_mundo(
        self,
    ):  # el "self" es necesario para que FastAPI pueda reconocer el método
        return {
            "message": "API de entretenimiento - EntertainAPI",
            "description": "EntertainAPI es una interfaz de programación de aplicaciones (API) diseñada para ofrecer acceso fácil y rápido a una amplia variedad de datos relacionados con entretenimiento, incluyendo información sobre películas, series, animes, mangas y más.",
            "endpoints": { 
                "anime": {
                    "AnimeFLV": {
                        "episodios_recientes": "/api/anime/animeflv/episodios-recientes",
                        "ultimos_animes": "/api/anime/animeflv/ultimos-animes",
                        "directorio_animes": "/api/anime/animeflv/directorio-animes",
                        "buscar_anime": "/api/anime/animeflv/buscar-anime?anime_a_buscar=sword%20art%20online",
                    },},
                "peliculas": {}},
            "documentation": {"swagger": "/docs", "doc": "/redoc"},
            "code": 200,
        }
