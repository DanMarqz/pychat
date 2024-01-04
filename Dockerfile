FROM python:3.11.7-alpine3.19

WORKDIR /app
COPY . .

EXPOSE 5556

CMD ["python", "/app/server.py"]

