FROM python:3.9
ENV PYTHONUNBUFFERED=1

RUN apt-get -y update && \
    apt-get -y install build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY poetry.lock pyproject.toml ./

RUN pip install poetry
RUN poetry config virtualenvs.create false && \
    poetry install
