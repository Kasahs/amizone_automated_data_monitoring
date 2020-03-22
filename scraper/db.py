import mysql.connector

def establish_con(localhost,username,password,database):
    db = mysql.connector.connect(
        #auth_plugin = 'mysql_clear_password',
        host = localhost,
        user = username,
        password = password,
        database = database,
    )
    return db

def run_sql(db, sql):
    cursor = db.cursor()
    cursor.execute(sql)
    return cursor

# #db = establish_con("localhost","manik","sweetbread", "amizone")
# cnx = mysql.connector.connect(
#     user='manik', password='sweetbread',
#     host='localhost', database='amizone',
#     #auth_plugin='mysql_native_password'
# )
# mycursor = run_sql(cnx,"SELECT * FROM amizone.tt_data")
# cnx.commit()
# for x in mycursor:
#     print(x)
