Задача: необходимо разработать back-end сервиса новостей, в котором будет REST API  для получения новостей с комментариями.

Требования:
•	необходимо возвращать количество комментариев к каждой новости (поле "comments_count")
•	возвращать необходимо не удаленные записи (поле "deleted")
•	необходимо вернуть количество комментариев к текущей новости (поле "comments_count")
•	в случае, если новости с таким id нет, необходимо вернуть код ошибки - 404
•	в случае, если запись удалена (поле "deleted"), необходимо вернуть код ошибки - 404

Язык реализации Python (3.9 или старше).
Можно использовать фреймворки (Asyncio, AioHTTP, FastAPI)

Даны файлы news.json, в котором находится список новостей.

{
  "news": [
    {
      "id": 1,
      "title": "news_1",
      "date": "2024-01-01T20:56:35",
      "body": "The news",
      "deleted": false,
    },
  ],
  "news_count": 1,
}
​

comments.json, в котором находятся комментарии к новостям, сопоставление по полю "news_id".

{
  "comments": [
    {
      "id": 1,
      "news_id": 1,
      "title": "comment_1",
      "date": "2024-01-02T21:58:25",
      "comment": "Comment",
    },
  ],
  "comments_count": 1,
}
​

- GET "/" - возвращает список новостей следующего формата

{
  "news": [
    {
      "id": 1,
      "title": "news_1",
      "date": "2019-01-01T20:56:35",
      "body": "The news",
      "deleted": false,
      "comments_count": 1,
    },
  ],
  "news_count": 1,
}
​

- GET "/news/{id}" - возвращает новость по ее id

{
  "id": 1,
  "title": "news_1",
  "date": "2019-01-01T20:56:35",
  "body": "The news",
  "deleted": false,
  "comments": [
    {
      "id": 1,
      "news_id": 1,
      "title": "comment_1",
      "date": "2019-01-02T21:58:25",
      "comment": "Comment",
    },
  ],
  "comments_count": 1,
}
