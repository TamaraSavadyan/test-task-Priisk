# test-task-Priisk
**Тестовое задание для компании Ксеньеевский прииск.**
Тестовое задание состояло из 2х задач: 
1) Парсер для сайта [https://nedradv.ru/nedradv/ru/auction](https://nedradv.ru/nedradv/ru/auction) и сохранения результата в базе данных (postgresql).
Для парсинга использовался Selenium. Основная логика парсера находится в файле **task1_parser.py**. Логика работы с базо данных - **task1_database.py**.
Для запуска парсера достаточно прописать в командной строке:
```bash
python task1_parser.py
```
Результат парсинга сохраняется в файл **data.json**. Для записи полученных данных в БД необходимо прописать следующее:
```bash
python task1_database.py
```
2) Несколько sql запросов в существующую базу данных.
Решение 2-го задания лежит в файле **task2.sql**.


Наибольшие трудности вызвало написание парсера. Процесс работы над парсером был следующий:
1) Я изучила сайт [https://nedradv.ru/](https://nedradv.ru/nedradv/ru/auction)https://nedradv.ru/nedradv/ru/auction, оценила задачу.
2) Пыталась найти доступ к какому-нибудь АПИ, из которого fontend подгружает информацию. Искала в вкладке 'Просмотр кода страницы' вкладку network и пыталась найти АПИ, к которому производится GET запрос.
3) Решила парсить по элементам страницы с помощью Selenium.
4) Изучила какие элементы соответсвуют требованиям ТЗ. Затем по этим элементам парсила сайт с Selenium и записала данные в **data.json** файл.

Также пришлось посидеть, подумать над тем, как форматировать дату из строки в тип Date для записи в PostgreSQL.





