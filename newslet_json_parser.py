"""
UDV Test News Project
Functions library
by Egor Maksimov, 2024
---
*DEV* Make sure to check the file for !!! comments
"""

import json


def n_gen():
    return (data_entry for data_entry in js_dump.data_news['news'])
    
    
def c_gen():
    return (data_entry for data_entry in js_dump.data_comments['comments'])


def js_dump():

    f_news = open('news.json', encoding="utf-8")
    f_comments = open('comments.json', encoding="utf-8")

    js_dump.data_news = json.load(f_news)       # !!! Read the file line by line instead of the whole thing
    js_dump.data_comments = json.load(f_comments)

    f_news.close()
    f_comments.close()


def comments_count():

    c_count = {}        # Возвращаем словарь {id новости: кол-во комментов}, чтобы проверка занимала O(n)
    
    for c_entry in c_gen():
        n_id = c_entry['news_id']
        if n_id not in c_count.keys():
            c_count[n_id] = 1
        else:
            c_count[n_id] += 1
            
    return c_count


def news_records():     # Выгрузка всех новостей одним запросом

    js_dump()   # Обновление записей

    res = []
    c_count = comments_count()  # Cловарь {id новости: кол-во комментов}
    
    
    for n_entry in n_gen():
        count = c_count[n_entry['id']] if n_entry['id'] in c_count else 0   #Если комментариев нет, то 0
        n_entry['comments_count'] = count
        if not n_entry['deleted']:
            res.append(n_entry)
            
    return res


def news_id_set():

    js_dump()   # Обновление записей
    
    n_set = set()
    
    
    for n_entry in n_gen():
        if not n_entry['deleted']:
            n_set.add(n_entry['id'])
    
    return n_set

def news_select(news_id):

    js_dump()   # Обновление записей
    
    res = {}
    
    
    for n_entry in n_gen():
        if n_entry['id'] == news_id:
            res = n_entry
            break
    
    res['comments'] = []
    c_count = 0
    
    for c_entry in c_gen():
        if c_entry['news_id'] == news_id:
            del c_entry['news_id']
            res['comments'].append(c_entry)
            c_count += 1
    res['comments_count'] = c_count
    
    return res
    