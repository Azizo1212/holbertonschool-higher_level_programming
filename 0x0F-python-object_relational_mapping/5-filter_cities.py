#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities of that stat"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],passwd=argv[2],db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities\
                   INNER JOIN states ON cities.state_id = states.id\
                   WHERE states.name = %s ORDER BY cities.id",
                   (argv[4], ))

    row = cursor.fetchall()
    new = 0
    for woof in row:
        if new != 0:
            print(", ", end="")
        print("%s" % woof, end="")
        new = new + 1
    print("")
    cursor.close()
    db.close()
