"""Автозапчастини визначаються маркою, моделлю та роком випуску автомобіля,
належать до певної категорії, мають назву та код. Програма повинна забезпечити
додавання/зміну/видалення автомобіля, додавання/зміну/видалення запчастини автомобіля, пошук
запчастин за назвою або категорією, приймання замовлення від клієнта на автозапчастини та
формування специфікації з переліком запчастин та цін у форматі JSON.
Дані про автомобілі, запчастини, замовлення зберігаються у базі даних"""

import os
import sqlite3
import json

db_filename = "data/data.db"


def create_db_from_zero():
    if os.path.exists(db_filename):
        os.remove(db_filename)
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE "cars" (
            "car_id"	INTEGER NOT NULL UNIQUE,
            "car_brand"	TEXT,
            "car_model" TEXT,
            "year"      INTEGER,
            PRIMARY KEY("car_id" AUTOINCREMENT)
        );
        """
    )  # todo deletion
    cursor.execute(
        """
        CREATE TABLE "parts" (
            "part_id"   INTEGER,
            "part_code"	TEXT NOT NULL UNIQUE,
            "car_id"	INTEGER NOT NULL,
            "category"  TEXT,
            "name"      TEXT,
            "price"     REAL,
            PRIMARY KEY("part_id" AUTOINCREMENT),
            FOREIGN KEY("car_id") REFERENCES "car_id" ("cars") ON DELETE CASCADE
        );
        """
    )
    cursor.execute(
        """
        CREATE TABLE "bills" (
            "bill_id" INTEGER NOT NULL, 
            "date" TEXT,
            "phone" TEXT,
            PRIMARY KEY ("bill_id" AUTOINCREMENT)
        );
        """
    )
    cursor.execute(
        """
        CREATE TABLE "bill_items" (
            "id" INTEGER NOT NULL,
            "bill_id" INTEGER NOT NULL, 
            "part_id" INTEGER NOT NULL,
            "number" INTEGER,
            PRIMARY KEY ("id" AUTOINCREMENT),
            FOREIGN KEY("bill_id") REFERENCES "bill_id" ("bills"),
            FOREIGN KEY("part_id") REFERENCES "part_id" ("parts") ON DELETE NO ACTION
        );
        """
    )
    conn.commit()
    conn.close()


def add_car(car_brand, car_model, year):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO cars (
            car_brand, 
            car_model, 
            year
        ) 
        VALUES (?, ?, ?);
        """,
        (car_brand, car_model, year)
    )

    inserted_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return inserted_id


def update_car(car_id, car_brand, car_model, year):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """UPDATE cars 
        SET car_brand = (?), car_model = (?), year = (?)
        WHERE car_id = (?);
        """,
        (car_brand, car_model, year, car_id)
    )

    conn.commit()
    conn.close()


def delete_car(car_id):
    try:
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()

        cursor.execute("""DELETE from parts where car_id = ?""", (car_id,))
        cursor.execute("""DELETE from cars where car_id = ?""", (car_id,))

        conn.commit()
        conn.close()

    except sqlite3.Error as error:
        return "Failed to delete a car from db. Error:  " + str(error)


def get_car(car_id):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT * FROM cars 
            WHERE car_id = (?);
        """,
        (car_id, )
    )
    car_info = cursor.fetchone()
    #  print(car_info)

    conn.commit()
    conn.close()
    return car_info


def all_cars():
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT * FROM cars 
        """
    )
    cars_info = cursor.fetchall()

    conn.commit()
    conn.close()
    return cars_info


def add_part(part_code, car_id, category, name, price):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO parts (
            part_code, car_id, category, name, price
        ) 
        VALUES (?, ?, ?, ?, ?);
        """,
        (part_code, car_id, category, name, price)
    )

    inserted_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return inserted_id


def update_part(part_id, part_code, category, name, price):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """UPDATE parts
        SET part_code = (?), category = (?), name = (?), price  = (?)
        WHERE part_id = (?);
        """,
        (part_code, category, name, price, part_id)
    )

    conn.commit()
    conn.close()


def delete_part(part_id):
    try:
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()

        cursor.execute("""DELETE from parts where part_id = ?""", (part_id,))

        conn.commit()
        conn.close()
        return "part successfully deleted"

    except sqlite3.Error as error:
        return "Failed to delete a part from db. Error:  " + str(error)


def get_part(part_id):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT * FROM parts 
            WHERE part_id = (?);
        """,
        (part_id,)
    )
    part_info = cursor.fetchone()
    #  print(part_info)

    conn.commit()
    conn.close()
    return part_info


def print_part(part_id):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT * FROM parts 
            WHERE part_id = (?) 
        """,
        (part_id,)
    )
    part_info = cursor.fetchone()

    conn.commit()
    conn.close()
    return part_info


def name_search(name):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT * FROM parts 
            WHERE name LIKE (?) 
            COLLATE NOCASE;
        """,
        (name + '%',)
    )
    parts_info = cursor.fetchall()

    conn.commit()
    conn.close()
    return parts_info


def category_search(category):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT * FROM parts 
            WHERE category LIKE (?) 
            COLLATE NOCASE;
        """,
        (category + '%',)
    )
    parts_info = cursor.fetchall()

    conn.commit()
    conn.close()
    return parts_info


def add_bill(date, phone, order: dict):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO bills (
            date, 
            phone
        ) 
        VALUES (?, ?);
        """,
        (date, phone)
    )
    bill_id = cursor.lastrowid

    for part_id in order:
        cursor.execute(
            """
            INSERT INTO bill_items (
                bill_id,
                part_id,
                number
            ) 
            VALUES (?, ?, ?);
            """,
            (bill_id, part_id, order[part_id])
        )

    conn.commit()
    conn.close()
    return bill_id


def print_bill(bill_id):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT * FROM bills WHERE bill_id = (?)
        """,
        (bill_id,)
    )
    bill_info = cursor.fetchone()

    cursor.execute(
        """
            SELECT * FROM bill_items WHERE bill_id = (?)
        """,
        (bill_id,)
    )
    parts_info = cursor.fetchall()
    new_parts_info = ()
    for item in parts_info:
        part_id = item[2]
        cursor.execute(
            """
                SELECT part_code, name, price FROM parts WHERE part_id = (?)
            """,
            (part_id,)
        )
        additional_info = cursor.fetchone()
        new_parts_info += (item[2:] + additional_info, )

    bill_info += (new_parts_info,)

    conn.commit()
    conn.close()
    return bill_info


def bill_json(bill_id):
    bill_info = print_bill(bill_id)
    bill_list = [bill_info[1], bill_info[2]]
    for item in bill_info[3]:
        dct = {"part_code": item[2], "name": item[3], "price": item[4], "amount": item[1]}
        bill_list.append(dct)
    ans = json.dumps(bill_list, indent=4, ensure_ascii=False)
    return ans


def test_db():
    create_db_from_zero()
    car_1 = add_car("Dodge", "Viper GTS (SR II)", 1996)
    car_2 = add_car("Bentley", "Continental GT V8", 2021)
    car_3 = add_car("Infiniti", "FX 50", 2011)
    # update_car(car_1, "Dodge", "Viper GTS", 1996)

    add_part("as15", car_1, "engine", "Dodge 165 kg 2.9 l", 2000)
    add_part("sc69", car_2, "engine", "Bentley 175 kg 3.5 l", 2500)
    add_part("sl42", car_3, "engine", "Infiniti 230 kg 5.4 l", 1739.99)
    add_part("cp99", car_1, "fuel tank", "Dodge 49 l", 500)
    add_part("tt11", car_2, "fuel tank", "Bentley 55 l", 678)
    add_part("as96", car_3, "fuel tank", "Infiniti 79 l", 1010)
    add_part("ty90", car_1, "battery", "Dodge 6СТ-60", 1500)
    add_part("fk69", car_2, "battery", "Bentley 6СТ-80", 1700)
    add_part("fu00", car_3, "battery", "Infiniti 6СТ-30", 1678)

    # get_part(1)
    # print(all_cars())
    # print(category_search(""))

    bill_1 = add_bill("2020-12-05", "+380929541205", {1: 1, 3: 2})
    bill_2 = add_bill("2020-09-14", "+380129544209", {2: 1, 4: 2})
    # print(print_bill(bill_1))


if __name__ == '__main__':
    test_db()
    # delete_car(1)
