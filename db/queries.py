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
