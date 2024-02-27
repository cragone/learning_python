import psycopg2

host = "localhost"
database = "FakeDisco"
user = "TBD"
password = "TBD"

try:
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)

    cur = conn.cursor()

    query = "SELECT * from DiscoData WHERE processarea = %s"  
    cur.execute(query, ('PA1',))  # Corrected: Added comma to make it a tuple

    rows = cur.fetchall()

    for row in rows:
        print(row)

except Exception as e:
    print(f"error: {e}")

finally:
    if cur is not None:
        cur.close()  

    if conn is not None:
        conn.close()  

print("data retrieved")
