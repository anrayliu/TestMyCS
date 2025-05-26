from database import Database


def init_db(db):
    db.query("DROP TABLE IF EXISTS questions;")

    db.query('''CREATE TABLE questions (
                    qid integer PRIMARY KEY,
                    question text NOT NULL,
                    answer boolean NOT NULL
                );''')

    db.query('''CREATE TABLE explanations (
                    qid integer PRIMARY KEY,
                    explanation text NOT NULL
                );''')

    db.query('''
            INSERT INTO questions VALUES (1, 'Python is a weakly typed language.', false);
            INSERT INTO questions VALUES (2, 'SQL is turing complete.', true);
            INSERT INTO questions VALUES (3, 'Software made for different CPU architectures are not cross-compatible.', true);
            INSERT INTO questions VALUES (4, 'The BIOS boots into the operating system.', false);

            INSERT INTO explanations VALUES (1, 'Python is strongly, dynamically typed.');
            INSERT INTO explanations VALUES (4, 'The BIOS locates the bootloader, which then boots into the operating system.');
            ''')
    

if __name__ == "__main__":
    with Database() as db:
        init_db(db)
