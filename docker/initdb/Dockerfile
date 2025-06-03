FROM python:3.12-slim

RUN apt-get update && apt-get upgrade -y

RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN pip install psycopg2-binary==2.9.10 python-dotenv==1.1.0

COPY init_db.py .

CMD ["python", "init_db.py"]
