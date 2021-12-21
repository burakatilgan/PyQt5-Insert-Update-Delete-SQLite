import sqlite3 as sql

def main():
    try:
        db = sql.connect("kullanicikayit.db")
        print("db oluşuturuldu.")
    except:
        print("db hatası")
    finally:
        db.close()

if __name__ == "__main__":
    main()