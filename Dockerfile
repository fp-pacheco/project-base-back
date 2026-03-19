FROM python:3.13-slim

RUN apt-get update && apt-get install -y build-essential

WORKDIR /app
ENV PYTHONPATH=/app

COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src
COPY ./main.py ./main.py
COPY ./prisma ./prisma

RUN prisma generate

CMD ["python", "main.py"]