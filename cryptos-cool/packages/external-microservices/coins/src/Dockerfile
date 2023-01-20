FROM python:latest

WORKDIR /app
RUN pip install python-dotenv flask requests

COPY . .

CMD [ "python3", "main.py"]