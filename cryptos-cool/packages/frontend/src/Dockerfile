FROM python:latest

WORKDIR /app
RUN pip install python-dotenv requests django

COPY . .

CMD [ "python3", "./dashboard/manage.py", "runserver", "0.0.0.0:8000"]