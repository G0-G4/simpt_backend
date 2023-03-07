FROM python:3.10.10-slim

WORKDIR /usr/src/app/simpt

ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt /usr/src/app/simpt
RUN pip install -r requirements.txt

COPY simpt /usr/src/app/simpt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
