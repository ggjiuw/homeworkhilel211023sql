import sqlite3



with sqlite3.connect('hw_db.sqlite3') as connection:
    cursor = connection.cursor()


    query = """
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL UNIQUE,
            pages INTEGER NOT NULL CHECK (length(pages) > 0),
            price INTEGER NOT NULL CHECK (length(price) > 0)
        )
    """
    cursor.execute(query)


    name = 'Історія'
    pages = 56
    price = 99
    values = [name, pages, price]

    query = """
        INSERT INTO books(name, pages, price)
        VALUES (?, ?, ?)
    """
    cursor.execute(query, values)
    

    values = (
        ('Моя книга', '257', '499'),
        ('Не моя книга', '208', '399'),
        ('Його книга', '179', '100'),
        ('HTML/CSS/JavaScript', '634', '989'),
        ('C++', '478', '749'),
        ('Python', '312', '579'),
        ('Machine Learning', '787', '1599'),
        ('Тест книга', '78', '59'),
        ('ChatGPT', '687', '1299'),
        ('Всесвітня Історія', '143', '100'),
        ('Історія України', '256', '79'),
    )
    
    query = """
        INSERT INTO books(name, pages, price)
        VALUES (?, ?, ?)
    """
    cursor.executemany(query, values)
    

    query = """
        SELECT name, pages, price
        FROM books
        WHERE price > 100
    """
    result = cursor.execute(query)
    print(f'дорожчі за 100 грн\n{result.fetchall()}')


    query = """
        SELECT name, pages, price
        FROM books
        WHERE price > 0
        ORDER BY price
        LIMIT 3
    """
    result = cursor.execute(query)
    print(f'\n3 найдешевших\n{result.fetchall()}')

    query = """
        SELECT name, pages, price
        FROM books
        WHERE name LIKE '%Історія%'
        LIMIT 2
    """
    result = cursor.execute(query)
    print(f'\nІсторія\n{result.fetchall()}')


    query = """
        ALTER TABLE books
        ADD COLUMN barcode REAL
    """
    cursor.execute(query)


    query = """
        UPDATE books
        SET
            barcode = '0-00012'
        WHERE
            pages > 200
    """
    cursor.execute(query)


    query = """
        DELETE FROM books
        WHERE
            price = 100
    """
    cursor.execute(query)