import sqlite3 as sql

def main():
    try:
        db = sql.connect("kullanicikayit.db")
        cursor = db.cursor()
        sorgu = "Create table user(id int, name txt, surname txt, number txt, mail txt, city txt)"
        cursor.execute(sorgu)
        print("table created")
    except sql.Error as e:
        print("tablo olusuturulamadı.")
if __name__ == "__main__":
    main()