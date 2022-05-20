#!/usr/bin/python3
"""class states"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])

    curso = db.cursor()
    curso.execute("SELECT * FROM states WHERE name = %s
                ORDER BY states.id ASC".format(sys.argv[4]))

    rows = curso.fetchall()
    for row in rows:
        print(row)
