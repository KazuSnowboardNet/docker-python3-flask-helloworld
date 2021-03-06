FROM python:3.9

WORKDIR /app

COPY ./app /app

RUN pip install Flask

CMD ["python", "index.py"]

EXPOSE 80 2222