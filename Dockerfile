FROM python:3.10.17-slim

ARG DIRECTORY_ARG

ENV DIRECTORY=$DIRECTORY_ARG

WORKDIR /app

COPY ./ ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "--host", "0.0.0.0", "app.main:app", "--reload"]