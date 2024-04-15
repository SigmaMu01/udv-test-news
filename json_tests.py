"""
*DEV* To run tests: pytest json_tests.py -vv
"""

from newslet_json_parser import *

news_dict = {"news": [{
                "id": 1,
                "title": "news_1",
                "date": "2024-01-01T20:56:35",
                "body": "The news",
                "deleted": False}], 
            "news_count": 1}

comm_dict = {"comments": [{
                "id": 1,
                "news_id": 1,
                "title": "comment_1",
                "date": "2024-01-02T21:58:25",
                "comment": "Comment"}],
            "comments_count": 1}
            
news_records_dict = {
            "news": [{
                "id": 1,
                "title": "news_1",
                "date": "2024-01-01T20:56:35",
                "body": "The news",
                "deleted": False,
                "comments_count": 1}],
            "news_count": 1}
            
news_print_dict = {
                "id": 1,
                "title": "news_1",
                "date": "2024-01-01T20:56:35",
                "body": "The news",
                "deleted": False,
                "comments": [
                  {
                    "id": 1,
                    "news_id": 1,
                    "title": "comment_1",
                    "date": "2024-01-02T21:58:25",
                    "comment": "Comment"}],
                "comments_count": 1}

comm_count_dict = {
            1: 1}            
            
            
def test_open_1():
    a = n_open(path='news.json')
    b = n_open()
    assert  a == b
    
    
def test_open_2():
    a = c_open(path='news.json')
    b = n_open()
    assert  a == b


def test_news_records():
    n = news_dict['news']
    c = comm_dict['comments']
    res = news_records(n, c)
    final = {"news": res, "news_count": len(res)}
    assert final == news_records_dict


def test_comments_count():
    c = comm_dict['comments']
    assert comments_count(c) == comm_count_dict


def test_news_select():
    n = news_dict['news']
    assert news_select(n, 1) == (False, news_dict['news'][0])
    

def test_news_print():
    c = comm_dict['comments']
    entry = news_dict['news'][0]
    assert news_print(c, entry) == news_print_dict
