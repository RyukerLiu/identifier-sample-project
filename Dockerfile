FROM python:3.7.4-alpine

WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --dev

COPY entrypoint.sh ./
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
