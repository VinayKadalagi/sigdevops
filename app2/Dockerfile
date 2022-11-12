FROM python:3.7-alpine

ENV FLASK_APP=app/__init__.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY api app/
RUN pip install -r app/requirements.txt

EXPOSE 5000
CMD ["flask", "run"]
