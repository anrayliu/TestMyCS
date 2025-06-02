FROM python:3.12-slim

RUN apt-get update && apt-get upgrade -y

COPY requirements.txt .

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "--bind", "0.0.0.0:5001", "app:app"]
