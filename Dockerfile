FROM python:3.11.5-alpine

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn",  "app.main:app", "0.0.0.0:8000"]