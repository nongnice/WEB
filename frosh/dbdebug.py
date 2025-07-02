import sqlite3


def main():
    def selectdata():
        conn=sqlite3.connect('frosh.db', check_same_thread=False)
        cursor=conn.cursor()
        registrants=cursor.execute('select name, sport from registrants')
        registors=registrants.fetchall()
        print('name     sport')
        for registor in registors:
            print(registor[0])

    selectdata()

main()