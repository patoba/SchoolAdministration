from sshtunnel import SSHTunnelForwarder
import psycopg2

PORT = 5432
REMOTE_HOST = "132.248.51.117"
REMOTE_SSH_PORT = 2244
REMOTE_USERNAME = 'alumno04_db'
REMOTE_PASSWORD = 'Alumno41121!"'

with SSHTunnelForwarder((REMOTE_HOST, REMOTE_SSH_PORT),
        ssh_username=REMOTE_USERNAME,
        ssh_password=REMOTE_PASSWORD,
        remote_bind_address=('localhost', PORT),
        local_bind_address=('localhost', PORT)):
        try:
            # Connect to an existing database
            connection = psycopg2.connect(user="alumno04",
                                            password='Alumno41121!"',
                                            host="localhost",
                                            port="5432",
                                            database="hnos_rodriguez_olap")

            # Create a cursor to perform database operations
            cursor = connection.cursor()
            # Print PostgreSQL details
            print("PostgreSQL server information")
            print(connection.get_dsn_parameters(), "\n")
            # Executing a SQL query
            # cursor.execute("SELECT version();")
            cursor.execute("SELECT * from hechos")
            # Fetch result
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")


cursor = connection.cursor()
pg_select = "SELECT * FROM peliculas"

cursor.execute(pg_select)
# Execute and print the output
print("Selected rows from book table")
peliculas = cursor.fetchall()
df_peliculas = pd.DataFrame(peliculas, columns = ["c1", "c2"])
df_peliculas.to_csv("peliculas.csv", index = False)
