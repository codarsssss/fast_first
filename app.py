import fastapi
import database
import pydantic_models
import config


api = fastapi.FastAPI()

response = {"Ответ":"Который возвращает сервер"}


@api.get('/')
def index():
    return response


@api.get('/static/path')
def hello():
    return "hello"


@api.get('/user/{nick}')      # переменные в пути заключаются в фигурные скобки
def get_nick(nick):           # в функцию передаем эту переменную и работаем с ней дальше
    return {"user":nick}      # при запросе страницы вернет строку, которую мы вписали после последнего слеша


@api.get('/userid/{id:int}')  # мы можем задавать тип данных прямо в пути через двоеточие
def get_id(id):               # тут в пути обязательно должно быть число, иначе возникнет ошибка
    return {"user":id}


@api.get('/user_id/{id}')
def get_id2(id: int):         # либо же его можно задавать как тайп-хинт прямо в функции
    return {"user":id}      # возвращается число, а не строка, как было бы без объявления типа данных


@api.get('/user_id_str/{id:str}')
def get_id2(id):
    return {"user":id}

