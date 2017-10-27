FROM python:3.5

RUN mkdir /crossbar
COPY requirements.txt /crossbar
WORKDIR /crossbar
RUN pip install -r requirements.txt

RUN groupadd -r crossbar && useradd -r -g crossbar crossbar
EXPOSE 8081 8081

COPY . /crossbar

RUN chown -R crossbar .
USER crossbar

CMD ["crossbar", "start"]
