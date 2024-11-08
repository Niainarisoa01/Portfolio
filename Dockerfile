FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y nodejs npm && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt package.json package-lock.json* ./

RUN pip install --no-cache-dir -r requirements.txt
RUN npm install

COPY . .

RUN npm run build

ENV FLASK_APP=run.py
ENV FLASK_ENV=production

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"] 