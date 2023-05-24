FROM python:3.8-slim

WORKDIR /srv/app/

COPY app02.py .

CMD ["python", "app02.py"]