FROM python:3.11

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD bash -c "alembic upgrade head && uvicorn main:app --host=0.0.0.0 --port=8000 --forwarded-allow-ips=*"
