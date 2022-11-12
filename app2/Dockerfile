FROM python:3.7-alpine

ENV FLASK_APP=app/api/__init__.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY . app/
RUN pip install -r app/api/requirements.txt

EXPOSE 5000
CMD ["flask", "run"]
