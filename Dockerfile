FROM python:3.9-slim

COPY handlers handlers
COPY keyboards keyboards
COPY lib lib
COPY *.py ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# ENV TZ='Europe/Moscow'
# RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

CMD [ "python", "./app.py" ] 