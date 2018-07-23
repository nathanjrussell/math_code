import hashlib
import pymysql
import sys


def create_ring_tables_order(n):
    drop_table_sql = "DROP TABLE IF EXISTS operation_table_{0!s}".format(n)
    build_table_sql = "CREATE TABLE operation_table_{0!s} (operation CHAR(1), operation_hash BINARY(16), element SMALLINT UNSIGNED , ".format(n)
    build_table_sql += ",".join(["element_{0!s} SMALLINT UNSIGNED ".format(i) for i in range(1,n)])
    build_table_sql += ", primary key (operation, operation_hash, element))" 
    # Open database connection
    db = pymysql.connect("test.blackpathway.com","nathan","sff312_SFF#!@_$*%&$@#","rings" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    try:
      # Execute the SQL command
      cursor.execute(drop_table_sql)
      cursor.execute(build_table_sql)

      db.commit()
      # Fetch all the rows in a list of lists.
    except pymysql.Error, e:
        print "ERROR IN UPLOADING CODE"
        try:
            print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
        except IndexError:
            print "MySQL Error: %s" % str(e)
    # disconnect from server
    db.close()


create_ring_tables_order(4)
"""
year = sys.argv[1]

print "Building Team List For Cross reference "

game_data = []
team_dict = {}
with open("complete_team_list_{0!s}.csv".format(year)) as f:
        for line in f:
                text_list = line.split(",")
                if len(text_list) ==2:
                        team_number = text_list[0].strip()
                        team_hash_id = hashlib.md5(text_list[1].strip()).hexdigest().upper()
                        team_dict[team_number] = team_hash_id
"""
