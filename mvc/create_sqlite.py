import sqlite3

cx = sqlite3.connect("/Users/David/git/design_pattern/mvc/task.db")
cu = cx.cursor()
cu.execute(
    "create table task (id INTEGER PRIMARY KEY , name TEXT, status NUMERIC)"
)

cx.commit()
cx.close()
