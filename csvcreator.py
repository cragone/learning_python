import csv
import psycopg2



host = "localhost"
database = "FakeDisco"
user = "postgres"
password = "postgrespostgres"


conn = psycopg2.connect(host=host, database=database, user=user, password=password)

cur = conn.cursor()

query = "SELECT * from DiscoData"

cur.execute(query)

with open("out.csv", "w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cur.description]) # write headers
    csv_writer.writerows(cur)

