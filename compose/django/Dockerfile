FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN groupadd -r django \
    && useradd -r -g django django

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt \
    && rm -rf /requirements.txt

COPY ./compose/django/gunicorn.sh /
RUN sed -i 's/\r//' /gunicorn.sh \
    && chmod +x /gunicorn.sh \
    && chown django /gunicorn.sh

COPY . /app

RUN chown -R django /app

RUN mkdir /app/static
RUN chown -R django /app/static

USER django

WORKDIR /app

EXPOSE 8000