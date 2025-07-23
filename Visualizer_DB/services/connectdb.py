import psycopg2
from modeles.db_credentials import DBCredentials

def try_connect_db(credentials: DBCredentials):
    # Fonction technique qui tente juste la connexion
    conn = psycopg2.connect(
        dbname=credentials.dbname,
        user=credentials.user,
        password=credentials.password,
        host=credentials.host,
        port=credentials.port
    )
    conn.close()
