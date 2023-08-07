import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://example.com/nedradv/ru/auction"

# Send an HTTP request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Extract the data for each auction item
auction_items = []
for item in soup.find_all("div", class_="auction-item"):
    date = item.find("div", class_="date").text.strip()
    lot = item.find("div", class_="lot").text.strip()
    region = item.find("div", class_="region").text.strip()
    status = item.find("div", class_="status").text.strip()
    deadline = item.find("div", class_="deadline").text.strip()
    contribution = item.find("div", class_="contribution").text.strip()
    organizer = item.find("div", class_="organizer").text.strip()

    auction_items.append((date, lot, region, status, deadline, contribution, organizer))

# Display the extracted data
for item in auction_items:
    print(item)


import psycopg2

# Connect to the PostgreSQL database
connection = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_username",
    password="your_password"
)

# Create a cursor to execute SQL queries
cursor = connection.cursor()

# Create the table for auction items
create_table_query = '''
    CREATE TABLE IF NOT EXISTS auction_items (
        id SERIAL PRIMARY KEY,
        date DATE,
        lot TEXT,
        region TEXT,
        status TEXT,
        deadline DATE,
        contribution FLOAT,
        organizer TEXT
    )
'''

cursor.execute(create_table_query)

# Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()
