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
        ('Мартис', 599, 'images/fighter.jpg', 1)
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




if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()
    pprint(get_products())

