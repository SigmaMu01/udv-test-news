#!/usr/bin/env python3

"""
UDV Test News Project
by Egor Maksimov, 2024
---
*DEV* API Call: uvicorn newslet:news_app
*DEV* HTTP methods catalogue: http://127.0.0.1:8000/docs
*DEV* Make sure to check the file for !!! comments
-
*PRD* Адрес главной страницы: http://127.0.0.1:8000
*PRD* Адрес страницы новостей: http://127.0.0.1:8000/news/{id}
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import s_time                       # Функции, возвращающие текущее время
import sys
from newslet_json_parser import *   # Функции, возвращающие запросы новостей и комментариев:
                                    # n_gen(), c_gen(), news_records(n_gen, c_gen), news_select(n_gen, news_id), news_print(c_gen, n_entry), add_news(entry, path = 'news.json')

if sys.version_info[0] < 3 and sys.version_info[0] < 12:    # Проверка версии Python
    raise Exception("Python 3.12 or a more recent version is required.")    # ! Не проверено, но должно запускаться на 3.10

class News(BaseModel):
    """Форма для хранения новостей в news.json"""
    id: int | None = 0
    title: str
    date: str | None = ""
    body: str
    deleted: bool | None = False


news_app = FastAPI()    # Вызов API


@news_app.get("/")
async def root():

    res = news_records(n_gen(), c_gen())
    return {"news": res, "news_count": len(res)}


@news_app.get("/news/{news_id}")
async def read_news(news_id: int):

    deleted, entry = news_select(n_gen(), news_id)
    
    if deleted:
        raise HTTPException(status_code=404, detail="News deleted")
    elif not entry:
        raise HTTPException(status_code=404, detail="News not found")
    else:    
        return news_print(c_gen(), entry)


@news_app.post("/news/new")     # Используем Postman для имитации POST-запросов по HTTP-адресу
async def create_news(item: News):
    item.id = s_time.id()
    item.date = s_time.date()
    add_news(item)


@news_app.post("/news/{news_id}")   # Передаём через Postman /news/{news_id}?deleted=true
async def remove_news(news_id: int, delete: bool | None = False):

    if delete:
        delete_news(n_gen(), news_id)
