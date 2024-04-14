"""
UDV Test News Project
Functions library
by Egor Maksimov, 2024
---
*DEV* Make sure to check the file for !!! comments
"""

import json


f_news = open('news.json', encoding="utf-8")
f_comments = open('comments.json', encoding="utf-8")

data_news = json.load(f_news)
data_comments = json.load(f_comments)


def comments_count():

    c_count = {}        # Возвращаем словарь {id новости: кол-во комментов}, чтобы проверка занимала O(n)
    gen = (data_entry for data_entry in data_comments['comments'])
    
    for c_entry in gen:
        id = c_entry['news_id']
        if id not in c_count.keys():
            c_count[id] = 1
        else:
            c_count[id] += 1
            
    return c_count


def news_records():     # Выгрузка всех новостей одним запросом

    res = []
    c_count = comments_count()  # Cловарь {id новости: кол-во комментов}
    
    gen = (data_entry for data_entry in data_news['news'])
    
    for n_entry in gen:
        count = c_count[n_entry['id']] if n_entry['id'] in c_count else 0   #Если комментариев нет, то 0
        n_entry['comments_count'] = count
        if not n_entry['deleted']:
            res.append(n_entry)
            
    return res


f_news.close()
f_comments.close()
