"""
UDV Test News Project
Functions library
by Egor Maksimov, 2024
---
*DEV* Make sure to check the file for !!! comments
"""

import json


def n_gen(path = 'news.json'):
    """Генератор записей новостей из news.json"""
    
    f_news = open(path, encoding="utf-8")
    data_news = json.load(f_news)
    f_news.close()
    
    return (data_entry for data_entry in data_news['news'])
    
    
def c_gen(path = 'comments.json'):
    """Генератор записей комментариев из comments.json"""
    
    f_comments = open(path, encoding="utf-8")
    data_comments = json.load(f_comments)
    f_comments.close()
    
    return (data_entry for data_entry in data_comments['comments'])


def news_records(n_gen, c_gen):
    """Выгрузка всех новостей одним запросом"""

    res = []
    c_count = comments_count(c_gen)  # Cловарь {id новости: кол-во комментов}
        
    for n_entry in n_gen:
        count = c_count[n_entry['id']] if n_entry['id'] in c_count else 0   #Если комментариев нет, то 0
        n_entry['comments_count'] = count
        if not n_entry['deleted']:
            res.append(n_entry)
            
    return res


def comments_count(c_gen):

    c_count = {}    # Возвращаем словарь {id новости: кол-во комментов}, чтобы проверка занимала O(n)
    
    for c_entry in c_gen:
        n_id = c_entry['news_id']
        if n_id not in c_count.keys():
            c_count[n_id] = 1
        else:
            c_count[n_id] += 1
            
    return c_count
    

def news_select(n_gen, news_id):
    """Проверка состояния новости по {news_id}"""

    deleted = False
    found_entry = {}
    
    for n_entry in n_gen:
        if n_entry['id'] == news_id:
            if n_entry['deleted']:
                deleted = True
                break
            found_entry = n_entry
            break
                
    return (deleted, found_entry)


def news_print(c_gen, n_entry):
    """Запись {новость, комментарии} для /news/{news_id}"""
    
    res = n_entry
    res['comments'] = []
    c_count = 0
    
    for c_entry in c_gen:
        if c_entry['news_id'] == n_entry['id']:
            del c_entry['news_id']
            res['comments'].append(c_entry)
            c_count += 1
    res['comments_count'] = c_count
    
    return res
    