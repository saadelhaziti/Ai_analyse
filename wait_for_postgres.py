import time
import psycopg2
import sys

def wait_for_postgres(host, db, user, password, timeout=30):
    start_time = time.time()
    while True:
        try:
            conn = psycopg2.connect(
                dbname=db,
                user=user,
                password=password,
                host=host
            )
            conn.close()
            print("Postgres is ready.")
            return
        except psycopg2.OperationalError:
            if time.time() - start_time > timeout:
                print("Timed out waiting for PostgreSQL.")
                sys.exit(1)
            print("Waiting for Postgres...")
            time.sleep(1)

if __name__ == "__main__":
    host = sys.argv[1]
    db = sys.argv[2]
    user = sys.argv[3]
    password = sys.argv[4]
    wait_for_postgres(host, db, user, password)
