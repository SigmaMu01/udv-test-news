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
                                        #news_records, 

if sys.version_info[0] < 3 and sys.version_info[0] < 12:    # Проверка версии Python
    raise Exception("Python 3.12 or a more recent version is required.")    # !!! Check if Python 3.10 runs it okay

news_app = FastAPI()    # Вызов API


@news_app.get("/")
async def root():

    res = news_records()
    return {"news": res, "news_count": len(res)}


@news_app.get("/news/{item_id}")
async def read_news(item_id: int):

    news = {1: 'yay', 2: 'nay', 3: 'deleted'}
    if item_id not in news:
        raise HTTPException(status_code=404, detail="News not found")
    elif news[item_id] == 'deleted':
        raise HTTPException(status_code=404, detail="News deleted")
        
    return {"item": news[item_id]}
