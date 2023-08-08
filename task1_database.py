import psycopg2
import json
import re
from psycopg2 import sql
from datetime import datetime
from config import config


def extract_date_from_string(input_date: str):
    months = {
        'января': '01',
        'февраля': '02',
        'марта': '03',
        'апреля': '04',
        'мая': '05',
        'июня': '06',
        'июля': '07',
        'августа': '08',
        'сентября': '09',
        'октября': '10',
        'ноября': '11',
        'декабря': '12'
    }

    pattern = r'до (\d{2}) ([а-я]+) (\d{4}) года'
    match = re.match(pattern, input_date)

    if match:
        day = match.group(1)
        month = months.get(match.group(2))
        year = match.group(3)

        formatted_date = f'{day}/{month}/{year}'
        return formatted_date

    for ru_month, en_month in months.items():
        input_date = input_date.replace(ru_month, en_month)
    formatted_date = datetime.strptime(
        input_date, '%d %m %Y').strftime('%d/%m/%Y')

    return formatted_date


def convert_json_data(data: dict):
    converted_data = []

    for entry in data:
        date_str = entry['Дата']
        formatted_date = extract_date_from_string(date_str)

        try:
            deadline_str = entry['Срок подачи заявок']
            formatted_deadline = extract_date_from_string(deadline_str)
        except KeyError:
            formatted_deadline = 'Null'

        amount_str = entry['Взнос за участие в аукционе (руб)']
        amount = float(''.join(filter(str.isdigit, amount_str)))

        converted_entry = (
            formatted_date,
            entry['Участок'],
            entry['Регион'],
            entry['Статус'],
            formatted_deadline,
            amount,
            entry['Организатор']
        )

        converted_data.append(converted_entry)

    return converted_data


def connect_and_execute(data: list):
    connection = psycopg2.connect(
        user=config.user,
        password=config.password,
        host=config.host,
        port=config.port,
        database=config.database,
    )

    cursor = connection.cursor()

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS auction_items (
            id SERIAL PRIMARY KEY,
            date DATE,
            lot TEXT,
            region TEXT,
            status TEXT,
            deadline DATE,
            participation_fee NUMERIC(10, 2),
            organizator TEXT
        )
    '''
    cursor.execute(create_table_query)

    for entry in data:
        query = sql.SQL('''
            INSERT INTO Auctions (date, lot, region, status, deadline, participation_fee, organizator)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''')
        cursor.execute(query, entry)

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    with open('data.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    auction_data = convert_json_data(json_data)

    connect_and_execute(auction_data)
