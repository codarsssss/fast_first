import pydantic_models
import fastapi

api = fastapi.FastAPI()

fake_database = {'users': [
    {
        "id": 1,
        "name": "Anna",
        "nick": "Anny42",
        "balance": 15300
    },

    {
        "id": 2,
        "name": "Dima",
        "nick": "dimon2319",
        "balance": 160.23
    }
    , {
        "id": 3,
        "name": "Vladimir",
        "nick": "Vova777",
        "balance": 200.1
    }
], }


@api.post('/user/create')
def index(user: pydantic_models.User):
    """
    Когда в пути нет никаких параметров
    и не используются никакие переменные,
    то fastapi, понимая, что у нас есть аргумент, который
    надо заполнить, начинает искать его в теле запроса,
    в данном случае он берет информацию, которую мы ему отправляем
    в теле запроса и сверяет её с моделью pydantic, если всё хорошо,
    то в аргумент user будет загружен наш объект, который мы отправим
    на сервер.
    """
    fake_database['users'].append(user)
    return {'User Created!': user}


@api.get("/users/")
def get_users(skip: int = 0, limit: int = 10):
    """
    Аргументы skip(пропуск) и limit(ограничение) будут браться из пути,
    который запрашивает пользователь, добавляются они после знака
    вопроса "?" и перечисляются через амперсанд "&", а их значения
    задаются через знак равно "=", то есть, чтобы задать значения
    аргументам skip=1 и limit=10 нам нужно выполнить GET-запрос,
    который будет иметь путь "/users?skip=1&limit=10"
    """
    return fake_database['users'][skip: skip + limit]


@api.put('/user/{user_id}')
def update_user(user_id: int, user: pydantic_models.User = fastapi.Body()): # используя fastapi.Body() мы явно указываем, что отправляем информацию в теле запроса
    for index, u in enumerate(fake_database['users']): # так как в нашей бд юзеры хранятся в списке, нам нужно найти их индексы внутри этого списка
        if u['id'] == user_id:
            fake_database['users'][index] = user    # обновляем юзера в бд по соответствующему ему индексу из списка users
            return user
