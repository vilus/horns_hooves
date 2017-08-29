FROM python:3.5

RUN mkdir /django_backend
COPY requirements.txt /django_backend
WORKDIR /django_backend
RUN pip install -r requirements.txt

COPY . /django_backend
RUN ./manage.py test --debug-mode -v 2 --settings horns_hooves.settings.tests
RUN rm -f db.sqlite3 || :

EXPOSE 8000
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN chown -R uwsgi .
RUN chmod +x entrypoint.sh
USER uwsgi

ENTRYPOINT ["./entrypoint.sh"]
