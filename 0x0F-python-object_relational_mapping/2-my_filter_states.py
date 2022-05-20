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
            db=sys.argv[3]

    curso = db.cursor()
    curso.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}'
                   ORDER BY states.id ASC""")

    curso = cursor.format(argv[4])
    rows = cursor.fetchall()
    for row in rows:
        print(row)
