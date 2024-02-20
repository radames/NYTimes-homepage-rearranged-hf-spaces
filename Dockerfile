FROM node:20-slim as builder

RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code
COPY ./frontend /code/frontend
WORKDIR /code/frontend
RUN npm ci
RUN npm run build

FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    PYTHONPATH=$HOME/app \
    PYTHONUNBUFFERED=1 

WORKDIR $HOME/app

COPY --chown=user . $HOME/app
COPY --chown=user --from=builder /code/frontend/dist $HOME/app/dist

CMD ["python", "app.py"]