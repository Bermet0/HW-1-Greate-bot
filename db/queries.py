import sqlite3
from pathlib import Path
from pprint import pprint


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent / "db.sqlite")
    cursor = db.cursor()


def create_tables():
    cursor.execute(
        """
        DROP TABLE IF 
        EXISTS category
        """
    )
    cursor.execute(
        """
        DROP TABLE IF 
        EXISTS products
        """
    )
    cursor.execute(
        """
        DROP TABLE IF 
        EXISTS follow
        """
    )
    cursor.execute('''DROP TABLE IF EXISTS house''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS house (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        descr TEXT,
        price INT,
        url TEXT,
        img TEXT
        )
        ''')
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS follow (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Questionaire (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        gender TEXT,
        meet_play INTEGER
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS category (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price DECIMAL,
            image TEXT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES category (id) 
        )
        """
    )
    db.commit()


def populate_tables():
    cursor.execute(
        """
        INSERT INTO category (name) VALUES 
        ('Герои'), ('Скины')
        """
    )
    cursor.execute(
        """
        INSERT INTO products (name, price, image, category_id) VALUES 
        ('Фанни', 399, 'images/jungler.jpg', 1),
        ('Хилос', 599, 'images/tank.jpg', 1),
        ('Мартис', 599, 'images/fighter.jpg', 1),
        ('Кагура: Вишневая Чародейка', 699, 'images/mage.jpg', 2)
        """
    )
    db.commit()


def get_products():
    cursor.execute(
        """
        SELECT * FROM products
        """
    )
    return cursor.fetchall()


def get_product_by_category_id(category_id: int):
    cursor.execute(
        """
        SELECT * FROM products WHERE category_id = :cat_id
        """, {"cat_id": category_id}
    )

    return cursor.fetchall()


def get_product_by_category_name(cat_name: str):
    cursor.execute(
        """
        SELECT * FROM products WHERE category_id = 
        (
            SELECT id FROM category WHERE name = :cat_name
        )
        """, {"cat_name": cat_name}
    )
    return cursor.fetchall()


def get_products_with_category():
    cursor.execute(
        """
        SELECT p.name, c.name FROM products AS p JOIN category AS c ON p.category_id = c.id
        """
    )
    return cursor.fetchall()


def save_questionaire(data):
    print(data)
    cursor.execute(
        """
        INSERT INTO Questionaire (name, gender, meet_play)
        VALUES (:name, :gender, :meet_play)
        """, data
    )
    db.commit()


def follow(user_id: str, user_name: str):
    cursor.execute(
        '''
        INSERT INTO follow (user_id, user_name) VALUES (?, ?)
        ''', (user_id, user_name)
    )
    db.commit()


def get_follow():
    cursor.execute(
        '''
        SELECT * FROM follow
        '''
    )
    return cursor.fetchall()


def save_house(title, descr, price, url, img):
    data = {
        'title': title,
        'descr': descr,
        'price': price,
        'url': url,
        'img': img
    }

    cursor.execute('''
    INSERT INTO house (title, descr, price, url, img) VALUES
    (:title, :descr, :price, :url, :img)
    ''', data)


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()
    pprint(get_products())
    # pprint(get_product_by_category_id(1))
    # pprint(get_product_by_category_id(2))
    # pprint(get_products_with_category())
    # pprint(get_product_by_category_name("Герои"))
    # pprint(get_product_by_category_name("Скины"))
    # pprint(get_products_with_category())
