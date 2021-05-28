"""Скласти програму для роботи з базою даних, що містить комунальні платежі. У
БД зберігаються назви компаній, неформальні назви платежів, а також рахунки від
компаній разом з відомостями про оплату. Для кожного рахунку вказують: компанію,
неформальну назву платежу, дату рахунку, суму рахунку, дату оплати, суму оплати.
Реалізувати функції додавання компанії, додавання неформальної назви платежу,
додавання рахунку, сплати рахунку, показу усіх рахунків за заданий місяць та рік, а
також загальної суми рахунків та сплаченої суми."""

import os
import sqlite3

db_filename = "payments.db"


def create_db_from_zero():
    if os.path.exists(db_filename):
        os.remove(db_filename)

    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE "companies" (
            "comp_id"	INTEGER NOT NULL UNIQUE,
            "comp_name"	TEXT NOT NULL,
            PRIMARY KEY("comp_id")
        );
        """
    )

    cursor.execute(
        """
        CREATE TABLE "unofficial_names" (
            "unf_name_id"	INTEGER NOT NULL UNIQUE,
            "unf_name"	TEXT,
            PRIMARY KEY("unf_name_id" AUTOINCREMENT)
        );
        """
    )

    cursor.execute(
        """
        CREATE TABLE "bills" (
            "bill_id" INTEGER NOT NULL, 
            "comp_id" INTEGER,
            "unf_name_id" INTEGER,
            "bill_date" TEXT,
            "bill_sum" REAL,
            "pay_date" TEXT,
            "pay_sum" REAL,
            PRIMARY KEY ("bill_id" AUTOINCREMENT),
            FOREIGN KEY("unf_name_id") REFERENCES "unofficial_names" ("unf_name_id"),
            FOREIGN KEY("comp_id") REFERENCES "companies" ("comp_id")
        );
        """
    )

    conn.commit()
    conn.close()


def add_comp(comp_name):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO companies (
            comp_name
        ) 
        VALUES (?);
        """,
        (comp_name,)
    )

    inserted_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return inserted_id


def add_unf_name(name):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO unofficial_names (
            unf_name
        ) 
        VALUES (?);
        """,
        (name,)
    )

    inserted_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return inserted_id


def add_bill(comp_id, unf_name_id, bill_date, bill_sum):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO bills (
            comp_id, 
            unf_name_id, 
            bill_date, 
            bill_sum
        ) 
        VALUES (?, ?, ?, ?);
        """,
        (comp_id, unf_name_id, bill_date, bill_sum)
    )

    inserted_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return inserted_id


def pay_bill(bill_id, pay_date, pay_sum):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """UPDATE bills 
        SET pay_date = (?), pay_sum = (?)
        WHERE bill_id = (?);
        """,
        (pay_date, pay_sum, bill_id)
    )

    conn.commit()
    conn.close()


def show_bills(time):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM bills
        """
    )
    bills_info = cursor.fetchall()

    for bill in bills_info:
        if bill[3][3:] == time:
            print(bill)

    conn.commit()
    conn.close()


def sum_all():
    sum_bills, sum_payments = 0, 0
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM bills
        """
    )
    bills_info = cursor.fetchall()

    for bill in bills_info:
        sum_bills += bill[4]
        if bill[6] is not None:
            sum_payments += bill[6]

    conn.commit()
    conn.close()
    print("sum_bills = ", sum_bills)
    print("sum_payments = ", sum_payments)


if __name__ == '__main__':
    create_db_from_zero()

    comp_1_id = add_comp("Компания 1")
    comp_2_id = add_comp("Компания 2")

    utility_id = add_unf_name("Комуналка")
    water_id = add_unf_name("Вода")
    gas_id = add_unf_name("Газ")

    bill_1_id = add_bill(comp_1_id, utility_id, "28.05.2021", 2000)
    bill_2_id = add_bill(comp_2_id, water_id, "01.01.2020", 8271.84)
    bill_3_id = add_bill(comp_2_id, gas_id, "13.04.2021", 720)
    bill_4_id = add_bill(comp_1_id, utility_id, "17.04.2021", 1234.5)

    pay_bill(bill_4_id, "11.09.2001", 1235)
    pay_bill(bill_1_id, "12.12.1212", 2021.98)

    show_bills("04.2021")
    sum_all()
