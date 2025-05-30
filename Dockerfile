FROM python:3.12-slim

RUN apt-get update && apt-get upgrade -y

COPY requirements.txt .

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]

# docker run --env-file secrets.env -p 5001:5001 testmycs:latest
