import psycopg2
import os
from dotenv import load_dotenv


def populate_db():
    conn = psycopg2.connect(database=os.environ["DB_NAME"],
                              host=os.environ["DB_HOST"],
                              port=os.environ["DB_PORT"],
                              user=os.environ["DB_USER"],
                              password=os.environ["DB_PASSWORD"])
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS questions;")
    cur.execute("DROP TABLE IF EXISTS explanations;")

    cur.execute('''CREATE TABLE questions (
                    qid integer PRIMARY KEY,
                    question text NOT NULL,
                    answer boolean NOT NULL
                );''')

    cur.execute('''CREATE TABLE explanations (
                    qid integer PRIMARY KEY NOT NULL UNIQUE,
                    explanation text NOT NULL
                );''')

    # questions and answers below

    cur.execute('''
                INSERT INTO questions VALUES (1, 'In a Kubernetes GitOps workflow using Argo CD, if two separate applications manage overlapping Kubernetes resources (e.g., the same ConfigMap), Argo CD will automatically detect the conflict and prevent either application from applying changes until the overlap is resolved.', false);
                INSERT INTO explanations VALUES (1, 'Argo CD does not automatically detect or block overlapping resource management between applications. Both apps will attempt to apply their manifests, and the last one to sync will “win,” potentially overwriting changes made by the other.');
    ''')

    conn.commit()

    cur.execute('''
                INSERT INTO questions VALUES (2, 'In a Kubernetes cluster using etcd as its backing store, if you configure --quorum-read=false on the kube-apiserver, it allows the API server to read from any etcd member regardless of whether it has the most recent data, which can improve read performance but may result in stale reads during network partitions.', true);
    ''')

    conn.commit()

    cur.close()
    conn.close()


if __name__ == "__main__":
    load_dotenv()
    populate_db()
