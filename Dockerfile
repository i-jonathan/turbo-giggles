FROM python:3.11-alpine

RUN pip install --upgrade pip
RUN pip install fastapi
RUN pip install "uvicorn[standard]"
RUN pip install mysql-connector-python

WORKDIR /app

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8090"]