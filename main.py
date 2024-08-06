from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI()


@app.get('/user/{user_id}')
async def user_id_(user_id: int = Path(ge=1, le=100, discription='Enter User ID', example='33')) -> dict:
    return {"message": f'Вы вошли как пользователь № {user_id}'}

@app.get('/user/{username}/{age}')
async def user_username_(username: Annotated[str, Path(min_length=5, max_length=20, discription='Enter username', example='UrbanUser')],
                         age: int = Path(ge=18, le=120, discription='Enter age', example='24')) -> dict:
    return {"message": f'Информация о пользователе. Имя: {username}, Возраст: {age}'}