FROM python:3.13

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Открываем порт
EXPOSE 5100

CMD [ "python", "./API.py" ]
