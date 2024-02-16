import pymysql

def update(name, Email, message):
    connection = pymysql.connect(host='127.0.0.1', user="root", passwd="zz01912001", db="mysql", charset='utf8')
    cur = connection.cursor()
    cur.execute("USE tamsui_hipster")
    cur.execute("INSERT INTO message (name, Email, message) VALUES (\"%s\",\"%s\",\"%s\")", (name, Email, message))
    cur.connection.commit()
    cur.close()
    connection.close()

