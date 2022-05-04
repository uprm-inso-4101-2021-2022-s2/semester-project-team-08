import psycopg2

pg_config = {
    'user': 'dev',
    'password': 'password1',
    'dbname': 'lspdb',
    'dbport': 8083
}


def connect(self):
    connection_url = "dbname=%s user=%s password=%s port=%s " % (
        pg_config["dbname"],
        pg_config["user"],
        pg_config["password"],
        pg_config["dbport"]
    )

    self.conn = psycopg2.connect(connection_url)
