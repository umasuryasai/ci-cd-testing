### My test
FROM python:3.8.8
WORKDIR /src
RUN python --version
COPY requirements.txt /
RUN pip install -r /requirements.txt
ADD src /src
EXPOSE 5001
CMD ["python", "app.py"]
