#!/usr/bin/env python3

"""
UDV Test News Project
by Egor Maksimov, 2024
---
*DEV* Вызов API: uvicorn newslet:news_app --reload
-
*PRD* Вызов API: uvicorn newslet:news_app
*PRD* Адрес страницы: http://127.0.0.1:8000
"""

from fastapi import FastAPI
import json
import sys


if sys.version_info[0] < 3 and sys.version_info[0] < 10:    # Проверка версии
    raise Exception("Python 3.10 or a more recent version is required.")

news_app = FastAPI()    # Вызов API


@news_app.get("/")
async def root():
    return {"message": "Hello, News!"}