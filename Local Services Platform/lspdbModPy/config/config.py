import psycopg2

pg_config = {
    'user': 'rgbrxrbnbwvcms',
    'password': 'ab783f405efec187721a83ad116c2294030b0042d31f44c10f5a230c2dca7499',
    'dbname': 'd2vnagml99p2hc',
    'dbport': 5432,
    'host': 'ec2-34-227-120-79.compute-1.amazonaws.com'
}


def connect(self):
    connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (
        pg_config["dbname"],
        pg_config["user"],
        pg_config["password"],
        pg_config["dbport"],
        pg_config["host"]
    )

    self.conn = psycopg2.connect(connection_url)
