#!/usr/bin/env python3

"""
UDV Test News Project
by Egor Maksimov, 2024
---
*DEV* Вызов API: uvicorn newslet:news_app
*DEV* Каталог GET-запросов: http://127.0.0.1:8000/docs
*DEV* Make sure to check the file for !!! comments
-
*PRD* Адрес главной страницы: http://127.0.0.1:8000
*PRD* Адрес страницы новостей: http://127.0.0.1:8000/news/{id}
"""

from fastapi import FastAPI, HTTPException
import sys
from newslet_json_parser import *     # Функции, возвращающие запросы новостей и комментариев:
                                        #news_records(), news_id_set(), news_select(news_id)

if sys.version_info[0] < 3 and sys.version_info[0] < 12:    # Проверка версии Python
    raise Exception("Python 3.12 or a more recent version is required.")    # !!! Check if Python 3.10 runs it okay

news_app = FastAPI()    # Вызов API


@news_app.get("/")
async def root():

    res = news_records()
    return {"news": res, "news_count": len(res)}


@news_app.get("/news/{news_id}")
async def read_news(news_id: int):

    news_set = news_id_set()
    
    if news_id not in news_set[0]:
        raise HTTPException(status_code=404, detail="News not found")
    elif news_id in news_set[1]:
        raise HTTPException(status_code=404, detail="News deleted")
    else:    
        return news_select(news_id)
