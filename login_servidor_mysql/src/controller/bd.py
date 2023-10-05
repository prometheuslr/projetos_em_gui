import mysql.connector

def logar_server(h,u,p,d):
    host = h
    user = u
    password = p
    database = d

    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )


    cursor = connection.cursor()
    def buscar_user(email):
        cursor.execute(f"SELECT * FROM user WHERE email = '{email}'")
        results = cursor.fetchall()
        print(results)
    def add_user():
        pass

    buscar_user("joa@email.com")

logar_server("localhost","root","Ar@gon.lrs2522","user_database")
