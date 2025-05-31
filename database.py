import psycopg2
import os


class Database:
    def __init__(self):
        self.connected = False
        
        self._conn = None 
        self._cur = None

        self.connect()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __del__(self):
        self.close()

    def connect(self):
        if not self.connected:
            self._conn = psycopg2.connect(database=os.environ["DB_NAME"],
                                host=os.environ["DB_HOST"],
                                port=os.environ["DB_PORT"],
                                user=os.environ["DB_USER"],
                                password=os.environ["DB_PASSWORD"])
            self._cur = self._conn.cursor()
            self.connected = True

    def close(self):
        if self.connected:
            self._cur.close()
            self._conn.close()
            self.connected = False

    def query(self, q, all=False):
        if not self.connected:
            raise Exception("Not connected.")

        try:
            self._cur.execute(q)
        except psycopg2.Error as e:
            self._conn.rollback()
            raise e

        self._conn.commit()

        if q.startswith("SELECT") or q.startswith("select"):
            return self._cur.fetchall() if all else self._cur.fetchone()
