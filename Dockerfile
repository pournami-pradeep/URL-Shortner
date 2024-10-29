FROM python:3.10-alpine

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000
ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]