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
    curso.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s ORDER BY cities.id", (sys.argv[4], ))

    rows = curso.fetchall()
    new = 0
    for i in row:
        if new != 0:
            print(", ", end="")
        print("%s" % i, end="")
        new = new + 1
    print("")

    curso.close()
    db.close()
