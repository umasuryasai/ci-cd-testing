FROM python:3.9-alpine
WORKDIR /src
COPY requirements.txt /
RUN pip install -r /requirements.txt
ADD src /src
EXPOSE 5001
CMD ["python", "app.py"]