FROM python:3.9
ENV PYTHONUNBUFFERED=1

RUN apt-get -y update && \
    apt-get -y install build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY poetry.lock* pyproject.toml ./

RUN pip install --upgrade pip && \
    pip install pipx
RUN pipx install poetry
ENV PATH /root/.local/bin:/root/.local/pipx/venvs/poetry/bin:$PATH
RUN pipx install poetry-dynamic-versioning
# RUN pip install --upgrade pip && \
#     pip install poetry poetry-dynamic-versioning
RUN poetry config virtualenvs.create false && \
    poetry install
