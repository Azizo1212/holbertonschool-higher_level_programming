#!/usr/bin/python3
"""lists all cities of that stateusing the database hbtn_0e_4_usa"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost'
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    curso = db.cursor()
    curso.execute("SELECT cities.name\
                FROM cities LEFT JOIN states\
                ON states.id = cities.state_id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (sys.argv[4],))

    rows = curso.fetchall()
    print(", ".join([row[0] for row in rows]))

    curso.close()
    db.close()
