import db
mydb=db.establish_con("localhost", "manik", "sweetbread", "amizone")
query = "SELECT class_time, class_loc, course_name FROM homepage_tt;"
mycursor=db.run_sql(mydb, query)
for (class_time, class_loc, course_name) in  mycursor:
    print("{} is at {} in {}".format(course_name, class_time, class_loc))
mydb.commit()
