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

    def connect(self):
        if not self.connected:
            self._conn = psycopg2.connect(database="postgres",
                                host="10.0.0.240",
                                port="5432",
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
            print(q)
        except psycopg2.Error as e:
            self._conn.rollback()
            raise e
        else:
            if q.startswith("SELECT") or q.startswith("select"):
                res = self._cur.fetchall() if all else self._cur.fetchone()
                self._conn.commit()
                return res
