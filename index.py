import psycopg2
# Update connection string information
host = "localhost"
dbname = "teste"
user = "postgres"
password = "postgres"
sslmode = "require"

# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()

def create_usuario(nome,email,senha):
    cursor.execute("INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s);", (nome, email, senha))

def find_all():
    cursor.execute("select * from usuario;")
    return cursor.fetchall()

def update_user(id,nome,email,senha):
    cursor.execute("UPDATE usuario SET nome = %s , email = %s, senha = %s WHERE id = %s;", (nome,email,senha,id))
   
def delete_user(id):
    cursor.execute("DELETE FROM usuario WHERE id = %s;", (id,))


delete_user(1)

conn.commit()
cursor.close()
conn.close()