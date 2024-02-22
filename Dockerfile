FROM python:3.9

ENV PYTHONUNBUFFRED = 1

WORKDIR /code

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "127.0.0.1:8000"]