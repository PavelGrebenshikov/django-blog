FROM python:3.8

ENV SECRET_KEY="HEllo"

WORKDIR /usr/src/my_django

COPY  requirements.txt /usr/src/my_django/
COPY . /usr/src/my_django/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "127.0.0.1:8000"]