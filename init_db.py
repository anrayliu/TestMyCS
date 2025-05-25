from database import Database


def init_db(db):
    db.query("DROP TABLE IF EXISTS questions;")

    db.query('''CREATE TABLE questions (
                    qid SERIAL PRIMARY KEY,
                    question text NOT NULL,
                    answer boolean NOT NULL
                );''')
    
    db.query('''
            INSERT INTO questions VALUES (DEFAULT, 'In a binary max-heap, the maximum element is always at the root.', true);
            INSERT INTO questions VALUES (DEFAULT, 'Dijkstra''s algorithm works correctly on graphs with negative edge weights.', false);
            INSERT INTO questions VALUES (DEFAULT, 'A greedy algorithm always provides an optimal solution.', false);
             ''')


if __name__ == "__main__":
    with Database() as db:
        init_db(db)
