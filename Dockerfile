FROM python:3.10-slim
RUN apt-get update && apt-get -y install libpq-dev gcc
WORKDIR /app/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["scripts/start.sh"]