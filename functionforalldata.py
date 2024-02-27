import psycopg2


host = "localhost"
database = "FakeDisco"
user = "TBD"
password = "TBD"

try:    
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)

    cur = conn.cursor()

    query = "SELECT * from DiscoData"

    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

except Exception as e:
    print(f"error: {e}")

finally:

    if cur is not None:
        cur.close()
    if conn is not None:
        cur.close()

print("data retrieved")
