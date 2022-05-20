#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])

    curso = db.cursor()
    curso.execute("SELECT cities.name FROM cities\
        JOIN states ON cities.state_id = states.id\
        WHERE states.name = %s\
        ORDER BY cities.id ASC", (sys.argv[4],))

    rows = cursor.fetchall()


    print(", ".join([row[0] for row in rows]))
    curso.close()
    db.close()
