FROM python:3.9
WORKDIR /code/src
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./src /code/src/
ENTRYPOINT [ "python3" ]
EXPOSE 8080
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
CMD ["main.py"]
