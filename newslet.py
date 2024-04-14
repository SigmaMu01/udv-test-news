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

from fastapi import FastAPI
import sys
from newslet_json_parser import *     # Функции, возвращающие запросы новостей и комментариев:
                                        #news_records, 

if sys.version_info[0] < 3 and sys.version_info[0] < 12:    # Проверка версии Python
    raise Exception("Python 3.12 or a more recent version is required.")    # !!! Check if Python 3.10 runs it okay

news_app = FastAPI()    # Вызов API


@news_app.get("/")
async def root():
    return {"news": news_records()}


#@news_app.get("/news/{id}")
#async def read_news():
#    return {"id": "Hello, "}
