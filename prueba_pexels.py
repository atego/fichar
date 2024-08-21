import json
import random
from requests import get

id_pexels: str = '563492ad6f91700001000001fedabb1b8d314a97913edf0474ea0f4c'
pagina = random.randint(1, 10)

respuesta_imagen: json = get(
    url=f'https://api.pexels.com/v1/search?query=landscape&page={pagina}',
    headers={'Authorization': id_pexels}
).json()

respuesta_frase: json = get(url='https://frasedeldia.azurewebsites.net/api/phrase').json()
print(respuesta_frase['phrase'])
print(respuesta_frase['author'])


print(respuesta_imagen['photos'][0]['src']['original'])
