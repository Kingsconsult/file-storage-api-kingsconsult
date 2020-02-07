FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ADD requirements.txt .
RUN pip install -r requirements.txt


RUN mkdir /app
WORKDIR /app
COPY file_storage . 


# EXPOSE 5000

# CMD python manage.py runserver 0.0.0.0:8000