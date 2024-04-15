from datetime import datetime


def id():

    return int(datetime.now().timestamp())  # Нет смысла парсить последний news_id, так как это делается для базы данных
    
    
def date():

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace(" ", "T")